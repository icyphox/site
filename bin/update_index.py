#!/usr/bin/env python3

from markdown2 import markdown_path
import os
import fileinput
import sys

# change our cwd
os.chdir("bin")

blog = "../pages/blog/"

# order files by recency
def getrecents(path):
    files = [path + f for f in os.listdir(blog) if f not in ["_index.md", "feed.xml"]]
    files.sort(
        key=lambda f: markdown_path(f, extras=["metadata"]).metadata["date"],
        reverse=True,
    )
    return files


def update_index(posts):
    path = "../pages/_index.md"
    with open(path, "r") as f:
        md = f.readlines()
    ruler = md.index("| --- | --: |\n")
    for post, i in zip(posts, range(4)):
        md[ruler + i + 1] = post + "\n"

    with open(path, "w") as f:
        f.writelines(md)


def update_blog(s):
    path = "../pages/blog/_index.md"
    s = s + "\n"
    for l in fileinput.FileInput(path, inplace=1):
        if "--:" in l:
            l = l.replace(l, l + s)
        print(l, end=""),


top_four = []
metas = []
lines = []
fnames = []

for i in range(4):
    top_four.append(getrecents(blog)[i])
    metas.append(markdown_path(getrecents(blog)[i], extras=["metadata"]).metadata)
    fnames.append(os.path.basename(os.path.splitext(getrecents(blog)[i])[0]))

for meta, fname in zip(metas, fnames):
    url = "/blog/" + fname
    lines.append(f"| [{meta['title']}]({url}) | `{meta['date']}` |")

update_index(lines)
update_blog(lines[0])
