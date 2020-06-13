#!/usr/bin/env python3

import jinja2
import subprocess
from jinja2 import DebugUndefined
import sys


def jinja_render(commit, date, big_commit, tmpl):
    template_loader = jinja2.FileSystemLoader("./")
    env = jinja2.Environment(loader=template_loader, undefined=DebugUndefined)
    try:
        template = env.get_template(tmpl)
    except jinja2.exceptions.TemplateNotFound:
        print("error: template not found")
        sys.exit(1)

    out = template.render(commit=commit, commit_date=date, big_commit=big_commit)
    return out


def get_commit():
    out = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"], 
            stdout=subprocess.PIPE)
    commit = out.stdout.decode("utf-8").strip()
    return commit

def get_big_commit():
    out = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            stdout=subprocess.PIPE
            )
    big_commit = out.stdout.decode("utf-8").strip()
    return big_commit


def get_commit_date(commit):
    out = subprocess.run(
            ["git", "show", "-s", "--format=%cd", "--date=short", commit],
            stdout=subprocess.PIPE)
    date = out.stdout.decode("utf-8").strip()
    return date


if __name__ == "__main__":
    commit = get_commit()
    big_commit = get_big_commit()
    date = get_commit_date(commit)
    rendered = jinja_render(commit, date, big_commit, "build/index.html")
    with open("build/index.html", "w") as f:
        f.write(rendered)
