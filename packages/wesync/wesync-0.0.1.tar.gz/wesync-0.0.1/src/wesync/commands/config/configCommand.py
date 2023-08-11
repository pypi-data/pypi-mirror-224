from wesync.commands.commandManager import CommandWithOperations


class ConfigCommand(CommandWithOperations):

    commandName = 'config'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self, **kwargs):
        super(ConfigCommand, self).run(**kwargs)

