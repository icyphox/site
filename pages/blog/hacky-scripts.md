---
template:
title: Hacky scripts
subtitle: The most fun way to learn to code
date: 2019-10-24
slug: hacky-scripts
---

As a CS student, I see a lot of people around me doing courses online
to learn to code. Don't get me wrong -- it probably works for some.
Everyone learns differently. But that's only going to get you so far.
Great you know the syntax, you can solve some competitive programming
problems, but that's not quite enough, is it? The actual learning comes
from _applying_ it in solving _actual_ problems -- not made up ones.
(_inb4 some seething CP bro comes at me_)

Now, what's an actual problem? Some might define it as real world
problems that people out there face, and solving it probably requires
building a product. This is what you see in hackathons, generally.

If you ask me, however, I like to define it as problems that _you_ yourself
face. This could be anything. Heck, it might not even be a "problem". It
could just be an itch that you want to scratch. And this is where
**hacky scripts** come in. Unclear? Let me illustrate with a few
examples.

## Now playing status in my bar

If you weren't aware already -- I rice my desktop. A lot. And a part of
this cohesive experience I try to create involves a status bar up at the
top of my screen, showing the time, date, volume and battery statuses etc.

So here's the "problem". I wanted to have my currently playing song
(Spotify), show up on my bar. How did I approach this? A few ideas
popped up in my head:

- Send `playerctl`'s STDOUT into my bar
- Write a Python script to query Spotify's API
- Write a Python/shell script to query Last.fm's API

The first approach bombed instantly. `playerctl` didn't recognize my
Spotify client and whined about some `dbus` issues to top it off.
I spent a while in that rabbit hole but eventually gave up.

My next avenue was the Spotify Web API. One look at the [docs](https://developer.spotify.com/documentation/web-api/) and
I realize that I'll have to make _more_ than one request to fetch the
artist and track details. Nope, I need this to work fast.

Last resort -- Last.fm's API. Spolier alert, this worked. Also, arguably
the best choice, since it shows the track status regardless of where
the music is being played. Here's the script in its entirety:

```shell
#!/usr/bin/env bash
# now playing
# requires the last.fm API key

source ~/.lastfm    # `export API_KEY="<key>"`
fg="$(xres color15)"
light="$(xres color8)"

USER="icyphox"
URL="http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks"
URL+="&user=$USER&api_key=$API_KEY&format=json&limit=1&nowplaying=true"
NOTPLAYING=" "    # I like to have it show nothing
RES=$(curl -s $URL)
NOWPLAYING=$(jq '.recenttracks.track[0]."@attr".nowplaying' <<< "$RES" | tr -d '"')


if [[ "$NOWPLAYING" = "true" ]]
then
	TRACK=$(jq '.recenttracks.track[0].name' <<< "$RES" | tr -d '"')
	ARTIST=$(jq '.recenttracks.track[0].artist."#text"' <<< "$RES" | tr -d '"')
	echo -ne "%{F$light}$TRACK %{F$fg}by $ARTIST"
else
	echo -ne "$NOTPLAYING"
fi
```

The `source` command is used to fetch the API key which I store at
`~/.lastfm`. The `fg` and `light` variables can be ignored, they're only
for coloring output on my bar. The rest is fairly trivial and just
involves JSON parsing with [`jq`](https://stedolan.github.io/jq/).
That's it! It's so small, but I learnt a ton. For those curious, here's
what it looks like running:

![](https://cdn.icyphox.sh/orGJ9.png)

## Update latest post on the index page

This pertains to this very blog that you're reading. I wanted a quick
way to update the "latest post" section in the home page and the
[blog](/blog) listing, with a link to the latest post. This would require
editing the Markdown [source](https://github.com/icyphox/site/tree/master/pages)
of both pages.

This was a very
interesting challenge to me, primarily because it requires in-place
editing of the file, not just appending. Sure, I could've come up with
some `sed` one-liner, but that didn't seem very fun. Also I hate
regexes. Did a lot of research (read: Googling) on in-place editing of
files in Python, sorting lists of files by modification time etc. and
this is what I ended up on, ultimately:

```python
#!/usr/bin/env python3

from markdown2 import markdown_path
import os
import fileinput
import sys

# change our cwd
os.chdir("bin")

blog = "../pages/blog/"

# get the most recently created file
def getrecent(path):
    files = [path + f for f in os.listdir(blog) if f not in ["_index.md", "feed.xml"]]
    files.sort(key=os.path.getmtime, reverse=True)
    return files[0]

# adding an entry to the markdown table
def update_index(s):
    path = "../pages/_index.md"
    with open(path, "r") as f:
        md = f.readlines()
    ruler = md.index("|  --  | --: |\n")
    md[ruler + 1] = s + "\n"

    with open(path, "w") as f:
        f.writelines(md)

# editing the md source in-place
def update_blog(s):
    path = "../pages/blog/_index.md"
    s = s + "\n"
    for l in fileinput.FileInput(path, inplace=1):
        if "--:" in l:
            l = l.replace(l, l + s)
        print(l, end=""),


# fetch title and date
meta = markdown_path(getrecent(blog), extras=["metadata"]).metadata
fname = os.path.basename(os.path.splitext(getrecent(blog))[0])
url = "/blog/" + fname
line = f"| [{meta['title']}]({url}) | `{meta['date']}` |"

update_index(line)
update_blog(line)
```

I'm going to skip explaining this one out, but in essence, it's **one
massive hack**. And in the end, that's my point exactly. It's very
hacky, but the sheer amount I learnt by writing this ~50
line script can't be taught anywhere.

This was partially how
[vite](https://github.com/icyphox/vite) was born. It was originally
intended to be a script to build my site, but grew into a full-blown
Python package. I could've just 
used an off-the-shelf static site generator
given that there are [so many](https://staticgen.com) of them, but
I chose to write one myself.

And that just about sums up what I wanted to say. The best and most fun
way to learn to code -- write hacky scripts. You heard it here.
