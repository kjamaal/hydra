import pytest
import os
from hydra.modules import environment


@pytest.fixture
def ansible_layout(tmp_path):
    return [
        os.path.abspath(
            tmp_path / 'test_ansible/inventories/production/group_vars'
        ),
        os.path.abspath(
            tmp_path / 'test_ansible/inventories/production/host_vars'
        ),
        os.path.abspath(
            tmp_path / 'test_ansible/inventories/stage/group_vars/hosts_vars'
        ),
        os.path.abspath(
            tmp_path / 'test_ansible/inventories/stage/group_vars/host_vars'
        ),
        os.path.abspath(
            tmp_path / 'test_ansible/inventories/production/hosts'
        ),
        os.path.abspath(
            tmp_path / 'test_ansible/inventories/stage/hosts'
        )
    ]


def test_fetch_file_system_permissions():
    current_dir = environment.fetch_file_system_permissions(os.getcwd())
    returns_error = environment.fetch_file_system_permissions("nonexistent")

    assert returns_error == 'is not directory'
    assert isinstance(current_dir, bool)


def test_write_project_layout(tmp_path, mocker, ansible_layout):
    mocker.patch('os.makedirs')
    environment.write_project_layout(ansible_layout)
    os.makedirs.assert_any_call(ansible_layout[0], exist_ok=True)


def test_execute_binaries():
    one_bin_one_arg = environment.execute_binaries(['ls -a'])
    one_bin_two_args = environment.execute_binaries(['ls -a -l'])
    two_bins_one_arg_each = environment.execute_binaries(['ls -a', 'file .'])

    assert one_bin_one_arg.returncode == 0
    assert one_bin_two_args.returncode == 0
    assert two_bins_one_arg_each.returncode == 0


def test_validate_project_dependencies():
    pass


def test_validate_project_layout():
    pass
