import logging
from wesync.projectManagers.common import CommonOperationsService
from wesync.services.snapshot import Snapshot


class WordpressOperationsService(CommonOperationsService):

    wpcli = None
    baseCommand = []

    def __init__(self, *args, **kwargs):
        super(WordpressOperationsService, self).__init__(*args, **kwargs)
        self.detectWPCLI()
        if self.wpcli is None:
            raise Exception("wp cli could not be found")

    def detectWPCLI(self):
        for testBinary in ["wp", "wp-cli", "wpcli"]:
            processResult = self.runCommand(["which", testBinary], ignoreRC=True)
            if processResult.returncode == 0:
                self.wpcli = testBinary
                break

        self.baseCommand = [self.wpcli, "--allow-root", "--path={}".format(self.deployment.get('path'))]

    def fullExport(self, snapshot: Snapshot):
        if self.artifactsConfig is None:
            self.exportWordpressFiles(snapshot.getPath('files.tar.gz'))
        else:
            self.exportArtifacts(snapshot)
        self.exportDatabase(snapshot.getPath('database.sql'))

    def fullImport(self, snapshot: Snapshot):
        if self.artifactsConfig is None:
            self.importWordpressFiles(snapshot.getPath('files.tar.gz'))
        else:
            self.importArtifacts(snapshot)
        self.importDatabase(snapshot.getPath('database.sql'))

    def exportDatabase(self, databaseExportFile):
        logging.info("Dumping Wordpress database at {} to {}".format(self.deployment.getPath(), databaseExportFile))

        args = self.baseCommand + ["db", "export", databaseExportFile, "--add-drop-table"]
        self.runCommand(args, cwd=self.deployment.getPath())

    def importDatabase(self, databaseImportFile):
        logging.info("Importing Wordpress database at {} to {}".format(databaseImportFile, self.deployment.getPath()))

        args = self.baseCommand + ["db", "import", databaseImportFile]
        self.runCommand(args, cwd=self.deployment.getPath())

    def exportWordpressFiles(self, archiveExportFile):

        exportRootDir = self.deployment.getPath() + "/wp-content"
        logging.info("Archiving Wordpress upload files at {} to {}".format(self.deployment.getPath(), archiveExportFile))

        args = ["tar", "-czf", archiveExportFile, '-C', exportRootDir, 'uploads']
        self.runCommand(args, cwd=self.deployment.getPath())

    def importWordpressFiles(self, archiveImportFile):
        importRootDir = self.deployment.getPath() + "/wp-content"
        importFilesDir = importRootDir + "/uploads"

        logging.info("Removing files directory at {}".format(importFilesDir))

        self.deletePath(importFilesDir, recursive=True)

        logging.info("Decompressing Wordpress files at {} to {}".format(archiveImportFile, self.deployment.getPath()))
        args = ["tar", "-xzf", archiveImportFile, '-C', importRootDir]
        self.runCommand(args, cwd=self.deployment.getPath())
