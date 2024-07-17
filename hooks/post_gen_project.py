#!/usr/bin/python3
import subprocess

try:
    subprocess.call(["pipx", "install", "hatch"])
    subprocess.call(["hatch", "env", "create"])
except Exception as e:
    print(f"An error occurred during initializing the git repo: {e}")
    print(
        "Makre sure to manually set up a git repository which is necessary for `hatch-vcs`"
    )
