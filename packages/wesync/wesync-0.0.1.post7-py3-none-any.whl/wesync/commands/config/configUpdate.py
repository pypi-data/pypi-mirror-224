import logging

from wesync.services.config.configManager import ConfigManager
from wesync.commands.operationManager import Operation
from wesync.services.config.remoteConfig import RemoteConfigService


class ConfigUpdateOperation(Operation):
    operationName = 'update'

    def __init__(self, config: ConfigManager):
        super().__init__()
        self.config = config

    def run(self):
        remoteConfigService = RemoteConfigService(self.config)
        remoteConfigService.fetchConfigRepository(force=True)
        hasChanges = remoteConfigService.hasChangesInConfigRepository()
        if hasChanges is True:
            remoteConfigService.pullConfigRepository()
        elif hasChanges is False:
            logging.info("No changes in remote repository")
