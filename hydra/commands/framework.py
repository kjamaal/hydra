import os


def validate_dependencies():
    return not any(os.scandir(os.getcwd()))


def write_project_layout(layout):
    for d in layout:
        os.makedirs(os.path.join(os.getcwd(), d))
