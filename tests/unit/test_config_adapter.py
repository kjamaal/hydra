from hydra.commands.adapters import config_adapter as config
from hydra.config import settings
from mock import patch


@patch.object(settings, 'from_env')
def test_fetch_project_config(getter, project_config_paths):
    getter.return_value = project_config_paths
    response = config.fetch_project_config('test')

    assert isinstance(response, dict)
    assert response['paths'] == ['test_path', 'test_path2']
