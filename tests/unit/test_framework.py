import os
from mock import patch
from hydra.commands import framework


@patch.object(os, "getcwd")
@patch.object(os, "scandir")
def test_validate_dependencies(os, cwd):
    os.return_value = [True]
    response = framework.validate_dependencies()

    os.assert_called_once()
    cwd.assert_called_once()
    assert not response


@patch.object(os, "getcwd")
@patch.object(os, "mkdir")
@patch.object(os.path, "join")
def test_write_project_layout(join, mkdir, path, tmp_path, project_layout):
    layout = []
    for i in project_layout:
        layout.append(
            tmp_path / i
        )
    framework.write_project_layout(layout)

    join.assert_called_once
    mkdir.assert_called_once
    path.assert_called_once
