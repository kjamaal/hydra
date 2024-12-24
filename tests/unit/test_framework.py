import os
from mock import patch
# from hydra.commands import framework


@patch.object(os, "scandir")
def test_validate_dependencies(os):
    # os.return_value = True
    # response = framework.validate_dependencies()

    # os.assert_called_once()
    # assert response
    pass


# TODO: tmpfile
def test_write_project_layout():
    pass
