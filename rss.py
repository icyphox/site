#!/usr/bin/env python3

import html
from markdown2 import markdown_path
import sys
import os

mdfile = sys.argv[1]
url =  os.path.splitext(mdfile)[0]
rendered = markdown_path(os.path.join('pages/blog/', mdfile), extras=['metadata', 
        'fenced-code-blocks', 'header-ids', 'footnotes', 'smarty-pants'])
meta = rendered.metadata
esc = html.escape(rendered)

item = f"""<item>
      <title>{meta['title']}</title>
      <description>{esc}</description>
      <guid isPermaLink="false">https://icyphox.sh/blog/{url}/</guid>
</item>
"""

print(item)
