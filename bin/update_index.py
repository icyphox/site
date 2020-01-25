#!/usr/bin/env python3

from markdown2 import markdown_path
import os
import fileinput
import sys

# change our cwd
os.chdir("bin")

blog = "../pages/blog/"

print("this is going to take a while...")
print("you might as well serve the site!")

# order files by recency
def get_recents(path):
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
    ruler = md.index("| :-- | --: |\n")
    for post, i in zip(posts, range(5)):
        md[ruler + i + 1] = post + "\n"

    with open(path, "w") as f:
        f.writelines(md)


def update_blog(s):
    path = "../pages/blog/_index.md"
    s = s + "\n"
    with open(path) as f:
        tempf = f.readlines()

    if s in tempf:
        print("index has already been updated. quitting...")
        sys.exit()
    for l in fileinput.FileInput(path, inplace=1):
        if "--:" in l:
            l = l.replace(l, l + s)
        print(l, end=""),


top_five = []
metas = []
lines = []
fnames = []

for i in range(5):
    top_five.append(get_recents(blog)[i])
    metas.append(markdown_path(get_recents(blog)[i], extras=["metadata"]).metadata)
    fnames.append(os.path.basename(os.path.splitext(get_recents(blog)[i])[0]))

for meta, fname in zip(metas, fnames):
    url = "/blog/" + fname
    new_line = f"| [{meta['title']}]({url}) | `{meta['date']}` |"
    lines.append(new_line)

#update_index(lines)
update_blog(lines[0])
