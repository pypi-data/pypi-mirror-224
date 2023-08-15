from wesync.services.config.configManager import ConfigManager
from wesync.services.initializationService import InitializationService
from wesync.commands.operationManager import Operation


class ConfigPurgeOperation(Operation):
    operationName = 'purge'

    def __init__(self, config: ConfigManager):
        super().__init__()
        self.config = config

    def run(self):
        initializationService = InitializationService(self.config)
        initializationService.purge()
