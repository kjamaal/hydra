#!/usr/bin/env python
from packaging.version import Version as v
import argparse
import subprocess
import requests


parser = argparse.ArgumentParser(description="build the hydra project")

parser.add_argument(
    "--build",
    action="store_true",
    help="build the hydra project"
)

parser.add_argument(
    "--version-bump",
    type=str,
    choices=['major', 'minor', 'patch', 'dev'],
    help="which semantic level should be bumped in the build"  # noqa
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
    print("\nmanage_project: Running without Tox. Use --tox to run tests.")

if args.build:
    print("\nmanage_project: Building hydra project...")

    if not args.version_bump:
        print("\nmanage_project: Build aborted. A new version level is required. Use --version-bump\n")  # noqa
    else:
        response = requests.get(
            'https://api.github.com/repos/kjamaal/hydra/releases/latest'
        )
        with open("hydra/__init__.py", "r") as mod:
            this_version = mod.read().split("= ")[1].replace("\"", "")
            if v(f"{this_version}") > v(response.json()["name"]):
                subprocess.run(
                    [
                        "python",
                        "-m",
                        "build"
                    ]
                )
            else:
                print("\nmanage_project: Build aborted. Currently Released version is higher. You should rebase it in and try to build/test again.")  # noqa
else:
    print("\nmanage_project: Running without Building. Give --build to build the hydra project")  # noqa

    #TODO: cleanup previous build artifacts in dist/
