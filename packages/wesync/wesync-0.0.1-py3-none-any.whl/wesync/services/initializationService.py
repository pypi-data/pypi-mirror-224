import logging
import os
from wesync.services.execute.localCommandExecutor import LocalCommandExecutor
from wesync.services.config.configManager import ConfigManager


class InitializationService:
    def __init__(self, config: ConfigManager):
        self.config = config
        self.executor = LocalCommandExecutor(config)

    def initAll(self):
        self.createWorkingDirectory()
        self.createConfigDirectory()
        self.createStashDirectory()
        self.cloneConfigRepository()

    def createWorkingDirectory(self):
        workdir = self.config.getWorkDir()
        if not os.path.exists(workdir):
            logging.info("Creating directory {}".format(workdir))
            self.executor.execute(["mkdir", "-p", "-v", workdir])

    def createConfigDirectory(self):
        configdir = self.config.getConfigDir()
        if not os.path.exists(configdir):
            logging.info("Creating directory {}".format(configdir))
            self.executor.execute(["mkdir", "-p", "-v", configdir])

    def createStashDirectory(self):
        stashdir = self.config.getStashDir()
        if not os.path.exists(stashdir):
            logging.info("Creating directory {}".format(stashdir))
            self.executor.execute(["mkdir", "-p", "-v", stashdir])

    def cloneConfigRepository(self):
        configdir = self.config.getConfigDir()
        if os.path.exists(configdir) and len(os.listdir(configdir)) == 0:
            configRepo = self.config.getConfigRepository()
            logging.info("Cloning config from {} into {}".format(configRepo, configdir))
            self.executor.execute(["git", "clone", configRepo, configdir])

