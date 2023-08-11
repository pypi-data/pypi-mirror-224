import logging
import os
import yaml
from collections import defaultdict
from wesync.services.config.sections.projectConfig import ProjectConfigData
from wesync.services.config.sections.deploymentConfig import DeploymentConfigData


class LocalConfigData:
    def __init__(self):
        self.defaults = {}
        self.aliases = defaultdict(lambda: {})
        self.projects = {}
        self.deployments = defaultdict(lambda: {})

    # Manage projects #
    def registerProjectName(self, projectName: str, projectConfigData: ProjectConfigData):
        self.projects[projectName] = projectConfigData

    def registerProject(self, projectConfigData: ProjectConfigData):
        projectName = projectConfigData.getName()
        logging.log(5, "Loading project {}: {}".format(projectName, projectConfigData))
        self.projects[projectName] = projectConfigData

    def getProjectByName(self, projectName: str):
        return self.projects.get(projectName)

    def getProjectByPath(self, path: str) -> ProjectConfigData:
        for project in self.projects.values():
            if project.get('path') and project.get('path') == path:
                return project
        for project in self.projects.values():
            if project.get('path') and project.get('path') in path:
                return project
        return None

    # Manage deployments #
    def registerDeployment(self, deploymentConfigData: DeploymentConfigData):
        project = deploymentConfigData.getProject()
        deploymentName = deploymentConfigData.getName()
        self.deployments[project.getName()][deploymentName] = deploymentConfigData

    def registerDeploymentName(self, deploymentName: str, deploymentConfigData: DeploymentConfigData):
        projectName = deploymentConfigData.getProjectName()
        self.deployments[projectName][deploymentName] = deploymentConfigData

    def getDeploymentsForProject(self, projectNameLookup: str) -> list:
        for projectName, deploymentDict in self.deployments.items():
            if projectName == projectNameLookup:
                return list(deploymentDict.values())
        return []

    def getDeploymentByName(self, projectName: str, deploymentName: str) -> DeploymentConfigData:
        return self.deployments.get(projectName, {}).get(deploymentName, None)

    def deleteDeployment(self, projectName: str, deploymentName: str):
        del(self.deployments[projectName][deploymentName])

    def getDeploymentByHostAndPath(self, host: str, path: str):
        for projectName, deploymentDict in self.deployments.items():
            for deploy in deploymentDict.values():
                if deploy.get('host') == host and deploy.get('path') == path:
                    return deploy
        return None

    # Configuration helpers #

    def isClean(self):
        for project in self.projects.values():
            if project.isClean() is False:
                return False
        return True

    def getDefaults(self, key: str, default=None):
        return self.defaults.get(key, default)

    def __getattr__(self, argument, default=None):
        return self.getDefaults(argument, default)


class LocalConfigManager:

    def __init__(self, configDirectory):
        self.configDirectory = configDirectory

    @staticmethod
    def _getfileLocation() -> str:
        configFileLocation = os.path.expanduser("~/wesync/config/")
        if os.path.exists(".wlkconfig.ini"):
            configFileLocation = ".wlkconfig.ini"
        elif os.path.exists(os.path.expanduser("~/.wlkconfig.ini")):
            configFileLocation = os.path.expanduser("~/.wlkconfig.ini")
        return configFileLocation

    def loadConfig(self) -> LocalConfigData:
        localConfigData = LocalConfigData()

        if not self.hasConfig():
            return localConfigData

        projectPath = self.configDirectory + "/projects"
        if not os.path.exists(projectPath):
            return localConfigData

        for project in os.listdir(projectPath):
            if ".yml" in project:
                with open(projectPath + "/" + project, "r") as fd:
                    projectConfigDict = yaml.safe_load(fd)

                project = ProjectConfigData()
                project.loadFromConfig(projectConfigDict)
                localConfigData.registerProject(project)

                for deploymentConfigDict in projectConfigDict.get('deployments', []):
                    deployment = DeploymentConfigData(project)
                    deployment.loadFromConfig(deploymentConfigDict)
                    localConfigData.registerDeployment(deployment)

        localConfigData.defaults = {}
        return localConfigData

    def hasConfig(self) -> bool:
        if not os.path.exists(self.configDirectory):
            return False
        if len(os.listdir(self.configDirectory)) == 0:
            return False

        return True
