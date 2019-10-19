#!/usr/bin/env python
import argparse
import subprocess


parser = argparse.ArgumentParser(description="build the hydra project")

parser.add_argument(
    "--build",
    action="store_true",
    help="build the hydra project"
)

parser.add_argument(
    "--tox",
    action="store_true",
    help="run tox before building"
)

args = parser.parse_args()

if args.tox:
    print("manage_project: running tox...\n")
    subprocess.run(
        [
            "tox"
        ]
    )
else:
    print("\nmanage_project: Running without Tox. Give --tox to run tests.")

if args.build:
    print("Building hydra project...")
    #TODO: import pyproject.toml and update values via configparser start with version  # noqa

    subprocess.run(
        [
            "python",
            "-m",
            "build"
        ]
    )
else:
    print("\nmanage_project: Running without Building. Give --build to build the hydra project")  # noqa

    #TODO: cleanup previous builds
