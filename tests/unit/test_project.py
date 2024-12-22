from hydra.modules import project
from hydra.config import settings
import hydra


def test_fetch_project_config():
    test = project.fetch_project_config('ansible')

    assert test
