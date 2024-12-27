import os
import shutil
from click.testing import CliRunner
from hydra.cli.main import create


def test_ansible():
    run = CliRunner()
    run.invoke(create, ['ansible'], input='y')

    assert os.path.isdir('ansible')

    if os.path.isdir('ansible'):
        shutil.rmtree('ansible')
