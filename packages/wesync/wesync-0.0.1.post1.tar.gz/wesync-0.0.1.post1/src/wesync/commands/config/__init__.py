from .configCommand import ConfigCommand
from .configInit import ConfigInitOperation
from .configPurge import ConfigPurgeOperation

ConfigCommand.availableOperations = [
    ConfigInitOperation,
    ConfigPurgeOperation
]

