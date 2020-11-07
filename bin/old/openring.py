#!/usr/bin/env python3
# openring.py - generate a webring from rss feeds

import feedparser
import arrow
import jinja2
import random
import sys
from lxml import html
from jinja2 import DebugUndefined

def jinja_render(html, tmpl):
    template_loader = jinja2.FileSystemLoader("./")
    env = jinja2.Environment(loader=template_loader, undefined=DebugUndefined)
    try:
        template = env.get_template(tmpl)
    except jinja2.exceptions.TemplateNotFound:
        print("error: template not found")

    out = template.render(feeds=html)
    return out


with open("feeds.txt") as f:
    feeds = f.readlines()

html_out = []

for f in random.sample(feeds, 3):
    fp = feedparser.parse(f)
    feed_link = fp.feed.link
    print(fp.feed.link)
    feed_title = fp.feed.title
    print(feed_title)
    full_summ = str(html.fromstring(fp.entries[0].summary).text_content())
    trunc_summ = full_summ[:256] + "…"
    pub_date = fp.entries[0].published
    pretty_date = arrow.get(pub_date, "ddd, DD MMM YYYY HH:mm:ss Z").format("MMM DD, YYYY")
    post_link = fp.entries[0].link
    post_title = fp.entries[0].title

    html_out.append(f"""<div class="openring-feed">
    <h4><a href="{post_link}">{post_title}</a></h4>
    <p>{trunc_summ}</p>

    <p>via <a href="{feed_link}">{feed_title}</a> on {pretty_date}</p>
    </div>
    """
    )

if sys.argv[1] == "-j":
    rendered = jinja_render(html_out, "templates/openring.html")
    with open("templates/text.html", "w") as t:
        t.write(rendered)
else:
    print(html_out)
