from click.testing import CliRunner
from hydra.cli.main import hydra


def test_hydra():
    run = CliRunner()
    result = run.invoke(hydra)

    assert not result.exception


def test_create():
    run = CliRunner()
    result = run.invoke(hydra, 'create')
    bad_result = run.invoke(hydra, 'nonexistent')

    assert not result.exception
    assert bad_result.exception


def test_version():
    run = CliRunner()
    result = run.invoke(hydra, 'version')

    assert isinstance(result.stdout, str)


def test_ansible():
    run = CliRunner()
    #TODO: figure out how to test this without side effects (actually creating directories) # noqa
    #result = run.invoke(hydra, 'create ansible -y')
    bad_result = run.invoke(hydra, 'create nonexistent')
    bad_result_2 = run.invoke(hydra, 'create ansible -no')

    #assert not result.exception
    assert bad_result.exception
    assert bad_result_2.exception
