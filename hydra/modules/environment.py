# from hydra.config import settings
import os
import subprocess


def fetch_file_system_permissions(path):
    """
    Verify that this instance can access the file system for read and write
    and that the root is empty

    args:

    path - str - the file system path to stat
    """
    if os.path.isdir(path):
        return not any(os.scandir(path))
    else:
        return "is not directory"


def write_project_layout(layout):
    """
    Create the given file system structure in the local file system

    args:

    layout - list - List of paths to create
    """
    for d in layout:
        os.makedirs(os.path.join(os.getcwd(), d), exist_ok=True)


def execute_binaries(binaries):
    """
    Execute commands to the operating system for the given binaries

    args:

    binaries - list - common separated strings containing the name
                      of each program and arguments to run
    """
    for command in binaries:
        proc_sig = command.split()
        proc_output = subprocess.run(proc_sig, capture_output=True)

    return proc_output


def validate_project_dependencies(project_type):
    """
    Validate that the file system and binary dependencies exist for the give
    project type

    args:

    project_type - str - the project to be checked
    """
    pass
