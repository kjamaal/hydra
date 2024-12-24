import hydra as h
import click
from hydra.commands import framework as f
from hydra.config import settings as config


@click.group(invoke_without_command=True)
@click.pass_context
def hydra(ctx):
    """A Project Initializer"""
    ctx.ensure_object(dict)


@hydra.group(invoke_without_command=True)
@click.pass_context
def create(ctx):
    """Create the selected project type"""
    ctx.ensure_object(dict)


@hydra.group(invoke_without_command=True)
@click.pass_context
def patterns(ctx):
    """List project patterns"""
    ctx.ensure_object(dict)


@hydra.group(invoke_without_command=True)
@click.pass_context
def list(ctx):
    """List all available single project types"""
    ctx.ensure_object(dict)


@hydra.command()
@click.pass_context
def version(ctx):
    """Show the current version"""
    print(h.VERSION)


@create.command()
@click.option("-y", "--yes-all", is_flag=True, help="yes to all prompts")
@click.pass_context
def ansible(ctx, yes_all):
    """Create an ansible project"""
    prompt = "y"

    if not f.validate_dependencies() and not yes_all:
        prompt = input(
            "This directory is not empty, would you like to continue anyway? (y/n)"  # noqa
        )

    if f.validate_dependencies() or prompt == "y" or yes_all:
        f.write_project_layout(config.from_env("ansible").paths)


@create.command()
@click.option("-a")
@click.pass_context
def cdk(ctx):
    """Create a cdk project"""
    pass


@create.command()
@click.option("-a")
@click.pass_context
def virtualbox(ctx):
    """Create a VirtualBox project"""
    pass


@create.command()
@click.option("-a")
@click.pass_context
def serverless_framework():
    """Create a serverless framework project"""
    pass


@create.command()
@click.option("-a")
@click.pass_context
def SAM():
    """Create a SAM cli project"""
    pass


@patterns.command()
@click.option("-a")
@click.pass_context
def python_ml():
    """
    Create a Machine Learning project using Python
    tooling
    """
    pass


@list.command()
@click.option("-a")
@click.pass_context
def project_types(ctx):
    """List project types"""
    pass


@list.command()
@click.option("-a")
@click.pass_context
def project_layouts(ctx):
    """List project file system layouts"""
    pass


if __name__ == "hydra.main":
    hydra(obj={})
