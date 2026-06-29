#!/usr/bin/env python3
print("test")
import os
import re
import subprocess
import sys

BASE_BRANCH = os.getenv("BASE_BRANCH", "main")
GITHUB_USER = os.getenv("GITHUB_USER")

if GITHUB_USER is None:
    print("No GitHub username found.")
    sys.exit(1)
print(f"Git USR: {GITHUB_USER}")

def fail(msg):
    print(f"ERROR: {msg}")
    sys.exit(1)


def run(cmd):
    return subprocess.check_output(cmd, text=True).strip()


# -----------------------------
# Find changed package files
# -----------------------------

changed = run([
    "git",
    "diff",
    "--name-only",
    f"origin/{BASE_BRANCH}...HEAD"
]).splitlines()

packages = [f for f in changed if f.startswith("packages/")]

if len(packages) == 0:
    print("No package changes.")
    sys.exit(0)


# -----------------------------
# Parse package header
# -----------------------------

header_re = re.compile(r'^([A-Z_]+)\s*=\s*[\'"]?(.*?)[\'"]?$')


def parse_package(path):
    data = {}

    with open(path, encoding="utf8") as f:
        for line in f:

            line = line.strip()

            if not line:
                continue

            if line.startswith("#"):
                continue

            m = header_re.match(line)

            if m:
                data[m.group(1)] = m.group(2)

            if "NAME" in data and "AUTHORS" in data:
                break

    return data


# -----------------------------
# Validate every package
# -----------------------------

for package in packages:

    filename = os.path.basename(package)

    pr = parse_package(package)

    if pr.get("NAME") != filename:
        fail(f"{filename}: NAME does not match filename.")

    #
    # Existing package?
    #
    exists = subprocess.run(
        [
            "git",
            "cat-file",
            "-e",
            f"origin/{BASE_BRANCH}:{package}"
        ]
    ).returncode == 0

    if not exists:
        print(f"{filename}: New package.")
        continue

    #
    # Read package from main
    #
    active_text = run([
        "git",
        "show",
        f"origin/{BASE_BRANCH}:{package}"
    ])

    active = {}

    for line in active_text.splitlines():

        line = line.strip()

        if line.startswith("#"):
            continue

        m = header_re.match(line)

        if m:
            active[m.group(1)] = m.group(2)

        if "NAME" in active and "AUTHORS" in active:
            break

    if active.get("NAME") != filename:
        fail(f"{filename}: Active package NAME mismatch.")

    authors = active.get("AUTHORS", "")

    #
    # ALL can modify
    #
    if "&ALL&" in authors:
        print(f"{filename}: Public package.")
        continue

    #
    # User authorized?
    #
    if f"&{GITHUB_USER}&" not in authors:
        fail(
            f"{filename}: {GITHUB_USER} is not a maintainer.\n"
            f"Maintainers: {authors}"
        )

    print(f"{filename}: OK")

print("Validation successful.")
