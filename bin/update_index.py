#!/usr/bin/env python3

from markdown2 import markdown_path
import os
import fileinput
import sys

# change our cwd
os.chdir('bin')

blog = '../pages/blog/'

# bunch of file hacks to get to the most recent file
def getrecent(path):
    files = [path + f for f in os.listdir(blog)
             if f not in ['_index.md', 'feed.xml']]
    files.sort(key=os.path.getmtime, reverse=True)
    return files[0]


def update_index(s):
    path = '../pages/_index.md'
    with open(path, 'r') as f:
        md = f.readlines()
    latest = md.index('# latest post\n')
    md[latest + 2] = s + '\n'

    with open(path, 'w') as f:
        f.writelines(md)


def update_blog(s):
    path = '../pages/blog/_index.md'
    s = s + '\n'
    for l in fileinput.FileInput(path, inplace=1):
        if "marker" in l:
            l=l.replace(l, l + s)
        print(l, end=''),
    
# fetch title and date
meta = markdown_path(getrecent(blog), extras=['metadata']).metadata
fname = os.path.basename(os.path.splitext(getrecent(blog))[0])
url = '/blog/' + fname
line = f"`{meta['date']}` [{meta['title']}]({url})"

update_index(line)
update_blog(line)


