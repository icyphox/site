---
template:
slug: site-changes
title: Site changes
subtitle: New stuff at the {back,front}end
date: 2020-05-27
---

The past couple of days, I've spent a fair amount of time tweaking this
site. My site's build process involves
[vite](https://github.com/icyphox/vite) and a bunch of
[scripts](https://github.com/icyphox/site/tree/master/bin). These
scripts are executed via vite's pre- and post-build actions. The big
changes that were made were performance improvements in the
`update_index.py` script, and the addition of `openring.py`, which you
can see at the very bottom of this post!

## speeding up index page generation

The old script -- the one that featured in [Hacky
scripts](/blog/hacky-scripts) -- was absolutely ridiculous, and not to
mention _super_ slow. Here's what it did:

- got the most recent file (latest post) by sorting all posts by
  `mtime`.
- parsed the markdown frontmatter and created a markdown table entry
  like: 

```python
line = f"| [{meta['title']}]({url}) | `{meta['date']}` |"
```
- updated the markdown table (in `_index.md`) by in-place editing the
  markdown, with the line created earlier -- for the latest post.
- finally, I'd have to _rebuild_ the entire site since this markdown
  hackery would happen at the very end of the build, i.e, didn't
  actually get rendered itself. 

That...probably didn't make much sense to you, did it? Don't bother.
I don't know what I was thinking when I wrote that mess. So with how it
_was_ done aside, here's how it's done now:

- the metadata for all posts are nicely fetched and sorted using
  `python-frontmatter`.
- the metadata list is fed into Jinja for use in templating, and is
  rendered very nicely using a simple `for` expression:

```
{% for p in posts %}
  <tr>
    <td align="left"><a href="/blog/{{ p.url }}">{{ p.title }}</a></td>
    <td align="right">{{ p.date }}</td>
  </tr>
{% endfor %}
```

A neat thing I learnt while working with Jinja, is you can use
`DebugUndefined` in your `jinja2.Environment` definition to ignore
uninitialized template variables. Jinja's default behaviour is to remove
all uninitialized variables from the template output. So for instance,
if you had:

```html
<body>
    {{ body }}
</body>

<footer>
    {{ footer }}
</footer>
```

And only `{{ body }}` was initialized in your `template.render(body=body)`,
the output you get would be:

```html
<body>
    Hey there!
</body>
<footer>

</footer>
```

This is annoying if you're attempting to generate your template across
multiple stages, as I was. Now, I initialize my Jinja environment like
so:

```python
from jinja2 import DebugUndefined

env = jinja2.Environment(loader=template_loader,undefined=DebugUndefined)
```

I use the same trick for `openring.py` too. Speaking of...let's talk
about `openring.py`!

## the new webring thing at the bottom

After having seen Drew's [openring](https://git.sr.ht/~sircmpwn/openring),
my [NIH](https://en.wikipedia.org/wiki/Not_invented_here) kicked in and I wrote
[`openring.py`](https://github.com/icyphox/openring.py). It pretty much
does the exact same thing, except it's a little more composable with
vite. Currently, it reads a random sample of 3 feeds from a list of
feeds provided in a `feeds.txt` file, and updates the webring with those
posts. Like a feed-bingo of sorts. ;)

I really like how it turned out -- especially the fact that I got my CSS
grid correct in the first try!
