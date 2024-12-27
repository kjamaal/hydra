import hydra as h
import click
from hydra.commands import framework as f
from hydra.commands.adapters import config_adapter as config


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
        f.write_project_layout(config.fetch_project_config("ansible")["paths"])


if __name__ == "hydra.main":
    hydra(obj={})
