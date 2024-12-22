"""
Module to manage project resources
"""


def fetch_project_layout(paths):
    """
    Return paths as a list of strings given a list of lists
    where each path itself is a list of strings.

    args:

    dirs - [list, list, ..] - list of paths to resolve
    """

    def resolve_path(path):
        if not paths:
            return []

        head, *tail = path
        return [head] + resolve_path(tail)

    def resolve_paths(paths):
        resolved_paths = []
        for path in paths:
            resolved_path = "/".join(resolve_path(path))
            resolved_paths.append(resolved_path)
        return resolved_paths

    return resolve_paths(paths)


def fetch_project_config(project_type):
    """
    Return default configuration for the given project type

    args:

    project_type - str - type name of the selected project to build
    """
    return True
