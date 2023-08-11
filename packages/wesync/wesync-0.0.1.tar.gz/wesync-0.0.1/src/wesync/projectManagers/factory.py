from wesync.projectManagers.drupal import DrupalOperationsService
from wesync.projectManagers.wordpress import WordpressOperationsService
from wesync.services.config.sections.deploymentConfig import DeploymentConfigData

from wesync.services.config.configManager import ConfigManager


def getProjectManagerFor(deployment: DeploymentConfigData, config: ConfigManager):
    project = deployment.getProject()
    projectType = project.get('type')
    if projectType == 'drupal':
        return DrupalOperationsService(deployment, config)
    elif projectType == 'wordpress':
        return WordpressOperationsService(deployment, config)

    raise ModuleNotFoundError("Could not find manager to handle {} project type".format(projectType))