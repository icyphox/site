#!/usr/bin/env python3

import os
import frontmatter as fm
import jinja2
from jinja2 import DebugUndefined


def get_metas(blog):
    all_metas = []
    files  = [ blog + f for f in os.listdir(blog) if f not in ["_index.md", "feed.xml"]]
    for f in files:
        with open(f) as fx:
            meta, _ = fm.parse(fx.read())
            all_metas.append(meta)
    
    all_metas.sort(key=lambda x: x['date'], reverse=True)
    return all_metas


def jinja_render(posts, tmpl):
    template_loader = jinja2.FileSystemLoader("./")
    env = jinja2.Environment(loader=template_loader, undefined=DebugUndefined)
    try:
        template = env.get_template(tmpl)
    except jinja2.exceptions.TemplateNotFound:
        print("error: template not found")

    out = template.render(posts=posts)
    return out


if __name__ == "__main__":
    all_metas = get_metas("pages/blog/")
    rendered = jinja_render(all_metas, "templates/_index.html") 
    with open("templates/index.html", "w") as f:
        f.write(rendered)
