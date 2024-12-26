import pytest


@pytest.fixture(scope="module")
def project_config_paths():
    return {
        'paths': ['test_path', 'test_path2']
    }


@pytest.fixture(scope="module")
def project_layout():
    return [
        'test/project/path1',
        'test/project/path2',
        'test/project/path2/sub_dir',
        'test/project/file.txt'
    ]
