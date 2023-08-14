import logging
from shutil import rmtree
from wesync.services.operations.commonOperations import CommonOperationsService
from wesync.services.snapshot import Snapshot


class DrupalOperationsService(CommonOperationsService):

    def __init__(self, *args, **kwargs):
        super(DrupalOperationsService, self).__init__(*args, **kwargs)
        self.path = self.deployment.getPath()

    def fullExport(self, snapshot: Snapshot):
        self.exportDatabase(snapshot)
        self.exportFiles(snapshot)

    def fullImport(self, snapshot: Snapshot):
        self.importDatabase(snapshot)
        self.importFiles(snapshot)

    def exportDatabase(self, snapshot: Snapshot = None):
        logging.info("Dumping Drupal database at {} to {}".format(self.path, snapshot.getPath()))
        databaseExportFile = snapshot.getPath('database.sql')

        if self.deployment.isLocal():
            self._exportLocalDatabase(databaseExportFile)
        else:
            self._exportRemoteDatabase(databaseExportFile)

    def _exportLocalDatabase(self, exportFilePath):
        args = ["drush", "sql:dump", "--root={}".format(self.path),
                "--extra-dump=--add-drop-table --set-gtid-purged=OFF --no-tablespaces --single-transaction=false",
                "--result-file={}".format(exportFilePath)
                ]
        self.runCommand(args, cwd=self.path)

    def _exportRemoteDatabase(self, exportFilePath):
        projectName = self.project.getName()
        tmpFileName = '/var/tmp/' + projectName + '-database.sql'
        args = ["drush", "sql:dump", "--root={}".format(self.path),
                "--extra-dump=--add-drop-table --set-gtid-purged=OFF --no-tablespaces --single-transaction=false",
                "--result-file={}".format(tmpFileName)
                ]
        self.runCommand(args, cwd=self.path)
        self.copyFrom(self.deployment, tmpFileName, )
        self.runCommand(["rm", tmpFileName])

    def importDatabase(self, snapshot: Snapshot):
        databaseImportFile = snapshot.getPath('database.sql')
        logging.info("Importing Drupal database at {} to {}".format(snapshot.getPath(), self.path))

        args = ["cat {} | drush sql-cli -root={}".format(databaseImportFile, self.path)]
        self.runCommand(args, cwd=self.path, shell=True)

    def exportFiles(self, snapshot: Snapshot):
        archiveExportFile = snapshot.getPath('files.tar.gz')
        exportRootDir = self.path + "/web/sites/default"

        logging.info("Archiving Drupal files at {} to {}".format(self.path, snapshot.getPath()))

        args = ["tar", "-czf", archiveExportFile, '-C', exportRootDir, 'files']
        logging.debug(args)

        if not self.config.get('dry-run'):
            self.runCommand(args, cwd=self.path)
            logging.info("Files dump finished")

    def importFiles(self, snapshot: Snapshot):
        archiveImportFile = snapshot.getPath('files.tar.gz')
        importRootDir = self.path + "/web/sites/default"
        importFilesDir = importRootDir + "/files"

        logging.info("Removing files directory at {}".format(importFilesDir))
        if not self.config.get('dry-run'):
            rmtree(importFilesDir, ignore_errors=True)

        logging.info("Decompressing Drupal files at {} to {}".format(snapshot.getPath(), self.path))
        args = ["tar", "-xzf", archiveImportFile, '-C', importRootDir]
        logging.debug(args)

        if not self.config.get('dry-run'):
            self.runCommand(args, cwd=self.path)
            logging.info("Files import finished")