---
template:
slug: 2020-in-review
title: 2020 in review
subtitle: Oh boy, here we go
date: 2020-12-24
---

It's been a little over 9 months since the day I left my university
dorms (got kicked out, rather), in light of <span class="lol">the
pandemic</span>. I have my finals going on right now, and 5 days to go
for the next examination -- a great time to reflect on what I managed to
do this year. So here I am, sitting at my little home office-thing, with
a bad cold -- as is tradition during December -- writing this post.
Let's get to it!


## interning at CometChat

I spent a good part of this year interning at
[CometChat](https://www.cometchat.com), mostly working as an
infrastructure engineer. I dabbled with some pretty neat tech -- here's
a quick list of things I worked on:

- XMPP over WebSockets (RFC 7395). Also wrote
    [wsabi](https://git.icyphox.sh/wsabi) -- a WebSocket proxy in Nim.
    Never got used, but cool nonetheless.
- On-premise (bare metal) deployment of our stack using Docker Swarm.
- Google Kubernetes Engine (GKE) deployment of our stack.

I think there's value in adding that I experienced a paradigm shift in
my view of tools like Kubernetes. I still think they're bloated and
abstraction heavy, but they exist to solve a problem -- and they do it
somewhat okay. In an ideal world, nobody would fall for the "cloud"
meme, and wouldn't toss everything into a container[^docker-meme] -- but
our world is far from that.

[^docker-meme]: https://i.imgur.com/3eTKEZp.jpg

## things I made

- [shlide](https://git.icyphox.sh/shlide): A slide deck presentation
    tool written in pure bash. Born from a conversation I had with a
    friend -- quickly hacked it together over a weekend. Even used it
    for a talk I presented!
- [vite](https://git.icyphox.sh/vite): Go rewrite of the static site
    generator I wrote in Python, way back in 2018. It was a misnomer,
    since it was far from _vite_.

## other hackery

Self-hosted a _bunch_ of services on my Pi. The only downtime is when my
ISP goes down, which is thankfully not _that_ often. Here's a list of
things running on my Pi right now:

- [radicale](https://radicale.org): Cal/CardDAV server
- [Pleroma](https://pleroma.social): Single-user federated social media
    instance
- [filehost](https://cdn.icyphox.sh)
- [gonic](https://github.com/sentriz/gonic): Music streaming server
- [crxn](http://deavmi.assigned.network/docs/crxn/site/): Cool network
    of cool people.
- Few other things that [Nerdy](https://peppe.rs) uses.

My OpenBSD install is still going strong! Started at 6.6, now on
6.8-current. This is most definitely my endgame OS -- everything just
works, and works very well.

I played [r2wars this year](/blog/r2wars-2020), which was hella fun. A
good exercise in assembly programming. I even placed 3rd, so that was
awesome.

## this blog

Evidently, this site has undergone quite a few visual changes. It's no
longer that all-black with white text, with occasional bits of cyan. My
overall aesthetic has considerably mellowed down -- prioritizing good
typography over colors.

```console
$ cat pages/blog/*.md | grep 'date: 2020-' | wc -l
      26
```

26 posts this year (including this)! That's 8 more than the 18 I wrote
last year -- roughly 1 post every two weeks. Pretty good variety too --
some technical, some less so...and some controversial. Heh.

## onward and upward

Contrary to popular opinion, 2020 wasn't all that bad -- obviously, I
only speak for myself. That said, I'm looking forward to 2021 for a
number of reasons: for one, I'll be done with college (finally!), and
starting a full-time job at a company I find really exciting!

I have a few blog post ideas that I didn't get around to writing this
year, so expect to see a few of those. The new job will involve a lot of
infra-related work -- I'm certain my incredibly sought after insights on
those things will find their way here, as well.

Anyway, I'm going to enjoy the rest of this year playing Runeterra and
Halo MCC. On to greater things in 2021, and I'll see you next year!
