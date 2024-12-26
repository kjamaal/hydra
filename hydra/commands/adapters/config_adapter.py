from hydra.config import settings


def fetch_project_config(project):
    """
    Return default configuration for the given project type

    args:

    project_type - str - type name of the selected project to build
    """
    return {"paths": settings.from_env(project)["paths"]}
