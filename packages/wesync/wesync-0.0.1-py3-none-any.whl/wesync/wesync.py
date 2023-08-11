#!/usr/bin/env python3
import sys

from wesync.common.logging import consoleLogging
import logging
from wesync.services.config.configManager import ConfigManager
from wesync.common.arguments import ArgumentParser
from wesync.commands.commandFactory import CommandFactory
from wesync.services.initializationService import InitializationService
from wesync.services.interaction.userInteraction import UserInteraction


def run():

    args = ArgumentParser().process().parse_args()
    configManager = ConfigManager(args)

    if configManager.get('debug') is True:
        consoleLogging.setLevel(5)

    if not configManager.localConfigManager.hasConfig():
        if UserInteraction().confirm("Configuration is missing. Create now ?", default=True) is True:
            initializationService = InitializationService(configManager)
            initializationService.initAll()
        else:
            sys.exit(0)

    configManager.initConfig()

    commandClass = CommandFactory.getCommandFor(configManager.getCommand())
    if not commandClass:
        logging.error("Could not find command manager for %s", configManager.getCommand())
        sys.exit(300)

    try:
        commandManager = commandClass(configManager)
    except Exception:
        logging.exception("Failed to initialize command class")
        sys.exit(100)

    try:
        commandManager.run()
    except Exception as e:
        if configManager.get('debug') is True:
            logging.exception(e, exc_info=e)
        else:
            logging.error(e)
        sys.exit(200)


if __name__ == '__main__':
    run()