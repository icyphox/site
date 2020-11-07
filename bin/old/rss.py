#!/usr/bin/env python3
# generate an rss item

import html
from myrkdown import markdown
import sys
import os
from collections import namedtuple
import re
import arrow
import operator
import warnings

# warnings.simplefilter("ignore", arrow.factory.ArrowParseWarning)
items_raw = []
from lxml import etree as ET


def convert_date(d):
    return arrow.get(d, "YYYY-MM-DD").format("ddd, DD MMM YYYY HH:mm:ss Z")


PREFIX_URL = "https://icyphox.sh/blog/"
link_extractor = re.compile("\/([^\/]*)\.md$")


def generate_node(rendered, path):

    item = ET.Element("item")
    title = ET.SubElement(item, "title")
    title.text = rendered.metadata["title"]
    description = ET.SubElement(item, "description")
    description.text = ET.CDATA(str(rendered))
    link = ET.SubElement(item, "link")
    link.text = PREFIX_URL + link_extractor.search(path).group(1)
    pubData = ET.SubElement(item, "pubDate")
    pubData.text = convert_date(rendered.metadata["date"])
    guid = ET.SubElement(item, "guid")
    guid.text = PREFIX_URL + link_extractor.search(path).group(1)

    return item


def parse_article(path):
    with open(path) as f:
        rendered = markdown(
            f.read(),
            extras=[
                "metadata",
                "fenced-code-blocks",
                "header-ids",
                "footnotes",
                "smarty-pants",
                "link-patterns",
            ],
            link_patterns=[
                (
                    re.compile(
                        r"((([A-Za-z]{3,9}:(?:\/\/)?)(?:[\-;:&=\+\$,\w]+@)?[A-Za-z0-9\.\-]+(:[0-9]+)?|(?:www\.|[\-;:&=\+\$,\w]+@)[A-Za-z0-9\.\-]+)((?:\/[\+~%\/\.\w\-_]*)?\??(?:[\-\+=&;%@\.\w_]*)#?(?:[\.\!\/\\\w]*))?)"
                    ),
                    r"\1",
                )
            ],
        )
        return (arrow.get(rendered.metadata["date"]), rendered, path)


tree = ET.parse(os.path.join("templates", "feed.xml"))
articles = []

for f in os.listdir("pages/blog/"):
    if f not in ["_index.md", "feed.xml"]:
        articles.append(parse_article(os.path.join("pages/blog", f)))

articles.sort(key=operator.itemgetter(0), reverse=True)
chan = tree.find("channel")

for article in articles:
    chan.append(generate_node(article[1], article[2]))

out = ET.tostring(tree, encoding="unicode")
with open("build/blog/feed.xml", "w") as f:
    f.write(out)
