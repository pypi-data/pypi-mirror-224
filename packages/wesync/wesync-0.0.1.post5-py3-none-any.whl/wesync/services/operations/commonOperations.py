import logging
import os.path
import re
from wesync.services.config.configManager import ConfigManager
from wesync.services.config.sections.deploymentConfig import DeploymentConfigData
from wesync.services.snapshot import Snapshot
from wesync.services.execute.localCommandExecutor import LocalCommandExecutor
from wesync.services.execute.remoteCommandExecutor import RemoteCommandExecutor


class CommonOperationsService:

    def __init__(self, deployment: DeploymentConfigData, config: ConfigManager):
        self.config = config
        self.deployment = deployment
        self.artifactsConfig = self.deployment.getProject().getArtifacts()
        self.project = self.deployment.getProject()
        self.executor = self.getExecutor()

    def getExecutor(self):
        if self.deployment.isLocal() is True:
            return LocalCommandExecutor(self.config)
        else:
            return RemoteCommandExecutor(self.config, self.deployment)

    def runCommand(self, args, **kwargs):
        if self.config.dryRun() is True:
            logging.info("Dry run: {} ({})".format(args, kwargs))
            return

        logging.debug(args)
        return self.executor.execute(args, **kwargs)

    def deletePath(self, path, recursive=False, force=False):
        args = ["rm"]
        if recursive is True:
            args += ["-r"]
        if force is True:
            args += ["-f"]
        args += [path]

        self.runCommand(args)

    # def copyFrom(self, deployment: DeploymentConfigData, sourcePath, destination):
    #     if isinstance(destination, Snapshot):
    #         destination = destination.getPath()
    #     elif not isinstance(destination, str):
    #         logging.error("copyFrom: destination must be a string or snapshot")
    #
    #     filetransfer = SCPFileTransfer(self.config)
    #     filetransfer.copyFromRemote(deployment, sourcePath, destination)
    #
    # def copyTo(self, source, deployment: DeploymentConfigData, destinationPath):
    #     if isinstance(source, Snapshot):
    #         source = source.getPath()
    #     elif not isinstance(source, str):
    #         logging.error("copyFrom: source must be a string or snapshot")
    #
    #     filetransfer = SCPFileTransfer(self.config)
    #     filetransfer.copyToRemote(source, deployment, destinationPath)

    def exportArtifacts(self, snapshot: Snapshot):
        for artifactConfig in self.artifactsConfig:
            if artifactConfig.get('type') == 'filepath':
                path = artifactConfig.get('path')
                name = artifactConfig.get('name')
                if not name or not path:
                    raise ValueError("Path or name missing from artifact config")
                snapshotPath = snapshot.getPath(name)
                self.exportFiles(snapshotPath, path)

    def importArtifacts(self, snapshot: Snapshot):
        for artifactConfig in self.artifactsConfig:
            if artifactConfig.get('type') == 'filepath':
                path = artifactConfig.get('path')
                name = artifactConfig.get('name')
                if not name or not path:
                    raise ValueError("Path or name missing from artifact config")
                snapshotPath = snapshot.getPath(name)
                self.importFiles(snapshotPath, path)

    def createPath(self, path):
        args = ["mkdir", "-p", "-v", path]
        self.runCommand(args)

    def cloneRepository(self, repositoryURL: str, branch: str = 'master'):
        args = ['git', 'clone', repositoryURL, '--branch', branch]
        logging.info("Cloning repository into" % repositoryURL)
        self.runCommand(args, cwd=self.project.get('path'))

    def createTempSnapshot(self) -> Snapshot:
        projectName = self.deployment.getProject().getName()
        tmpDirName = '/var/tmp/westash/' + projectName
        self.createPath(tmpDirName)
        remoteSnapshot = Snapshot(tmpDirName)
        return remoteSnapshot

    def exportFiles(self, archiveExportFile, path):
        path = os.path.normpath(re.sub(r'^(/+)', '', path))

        rootDir = self.deployment.getPath()
        pathDirectories = path.split("/")

        if len(pathDirectories) > 1:
            path = pathDirectories[-1]
            rootDir = rootDir + "/" + '/'.join(pathDirectories[:-1])

        logging.info("Archiving files at {}/{} to {}".format(rootDir, path, archiveExportFile))

        args = ["tar", "-czf", archiveExportFile, '-C', rootDir, path]
        self.runCommand(args, cwd=self.deployment.getPath())

    def importFiles(self, archiveImportFile, path):
        rootDir = self.deployment.getPath()

        path = os.path.normpath(re.sub(r'^(/+)', '', path))
        pathDirectories = path.split("/")

        if len(pathDirectories) > 1:
            path = pathDirectories[-1]
            rootDir = rootDir + "/" + '/'.join(pathDirectories[:-1])

        targetPath = rootDir + "/" + path
        logging.info("Removing files directory at {}".format(targetPath))

        self.deletePath(targetPath, recursive=True)

        logging.info("Decompressing files at {}/{} to {}".format(archiveImportFile, rootDir, path))
        args = ["tar", "-xzf", archiveImportFile, '-C', rootDir]
        self.runCommand(args, cwd=self.deployment.getPath())
