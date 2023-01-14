---
template:
slug: 2022-in-review
title: 2022 in review
subtitle: Late again because I was busy packing
date: 2023-01-14
---

Quite possibly the "fastest" year I've experienced -- it feels like
yesterday when 2022 began. I think I *did* a lot last year, contrary to
previous years where I felt I'd just squandered my time away. Which is
partly great because more content! But also not great, because I have to
write it. It's not that I don't enjoy writing anymore (despite what the
number of posts in 2022 might lead you to believe), I just find it
harder to sit and do the thing -- perhaps something to think about and
investigate in 2023. But I digress -- as I said, I did get a lot done
last year, so let's get right into it.

## projects & hacks

I'm only talking about software projects here, since this time around,
we've got some hardware hacks (ooh!).

First on the list is [legit](https://git.icyphox.sh/legit), a web
frontend for git. A very important characteristic of legit that *needs*
mention is the fact that it's written in Go -- it's even the name of the
first major release ([v0.2.0](https://git.icyphox.sh/legit/refs)).[^1]
On a more serious note, it's probably the nicest thing I've built from
scratch and it's very cool to see legit instances in the wild. I
consider it *mostly* feature complete, barring a couple of outstanding
PRs that I have yet to get to.

[^1]: Some folks on the red site
    [really](https://lobste.rs/s/trcln1/legit_web_frontend_for_git#c_ybjpfm)
    [didn't](https://lobste.rs/s/trcln1/legit_web_frontend_for_git#c_hgnuco)
    [like](https://lobste.rs/s/trcln1/legit_web_frontend_for_git#c_t4tl4w) it. :^)

Next up is [honk](https://git.icyphox.sh/honk). Not really my *own*
project, but something I spent a non-negligible amount of time hacking
on. The honk lives in my head, rent-free. A few changes in my honk fork
are:

- user profile pictures
- color scheme and UI
- pretty @ URLs (like https://h.icyphox.sh/@icy)
- bunch of other miscellaneous thingamajigs

Lastly, I [installed OpenBSD](/blog/openbsd-oci/) on my Oracle VM and
now everything runs off it, this site included.

Probably not a "project", but I'll include it here anyway: I switched my
entire [dotfiles](https://git.icyphox.sh/dotfiles) setup to Nix and
home-manager and rest of that shit I used to filter on Lobste.rs. While
I like the declarativeness, I won't pretend I understand the half of it.
Believe me, I've tried. But it mostly just works the way I have it, so
I'll leave it at that.

## keyboards: my (first) new expensive hobby

Normal 60% keyboards are out -- ergonomic split ortho keyboards are in.
I built three keyboards this year: the Lotus58, and two semi-custom
34-key wireless splits: the
[Ferricy](https://github.com/icyphox/ferricy), and the Ferricy Choc.

<div class="row">
<img src="https://cdn.icyphox.sh/F9YxI.jpeg" style="width: 500px"/>
<img src="https://cdn.icyphox.sh/rgVrx.jpeg" />
<img src="https://cdn.icyphox.sh/LUqg9.jpeg" />
</div>

There's a lot to write about keyboards and how I use mine, but I'll
likely write a separate post covering that since it's fairly
interesting and pretty long-winded. Until then, you can read [Nerdy's
article](https://peppe.rs/posts/programming_on_34_keys/) on the
subject.

## my time at Ory

Sometimes things don't work out and it's best to cut your losses and
bounce. I came away with only positives and I greatly enjoyed my time at
Ory. I got to work on some rather exciting stuff like:

- distributed tracing using OTel and Tempo
- centralized multi-cluster logging using Loki and Promtail
- tackling interesting engineering problems like caching sessions at
  edge
- a whole bunch more...

No ragrets.

## travel

A decent amount of travel last year: a week in Goa, three days in
Jaipur, two days in Chikmagalur and one day in New Delhi. Here's one
picture from each trip, in order.

<div class="row">
<img src="https://cdn.icyphox.sh/6CuTI.jpeg" />
<img src="https://cdn.icyphox.sh/96xo7.jpeg" />
<img src="https://cdn.icyphox.sh/xc9ty.jpeg" />
<img src="https://cdn.icyphox.sh/jxhk0.jpeg" />
</div>

## fitness

My fitness journey has seen considerable improvement. I streamlined my
routine for the most part, and I've stuck to it. My usual week now
consists of 3-4 upper body workouts, about 2 core workouts and 2 runs,
about 5 or 6km.

My ability to run has also greatly increased. I used to struggle to hit
5ks back in 2021 -- I can now comfortably run 8k and still feel pretty
good after. Granted, I'm not running for time -- my fastest 5k (the only
time I timed it) is a rather generous 26 minutes.

One major change I made in the latter half of last year was switching to
calisthenics for all my strength training. My ultimate goal is to be
able to do a full planche and front lever unassisted. I can currently
hold a tucked front lever for about 10 seconds -- but hey, progress is
progress.

2022 was the year I got decently shredded. Still not quite Chris Heria,
but we're getting there. I'd put myself somewhere around 15% body fat,
on a good day. I didn't *strictly* regulate my diet, but I was somewhat
conscious about what I was eating. A rough daily calorie estimate is
constantly in the back of my head. For '23, I'd like to be a little more
meticulous and properly count my calorie intake.

## reading

[Reading](/reading) was definitely on the forefront of 2022. I made a
conscious effort to spend a set amount of time each day reading -- until
about late November when I simply stopped. I can't remember why I did,
but for me, it's really easy to "lose" a habit -- week or two of not
reading, and I'll find myself moving on to other things. Another thing
to think about for 2023.

In 2022, I read 15 books (dropped one). I'm discounting *Assassin's
Apprentice* since I have yet to get around to finishing it. Looking
back, I can't pick any single standout read of last year, except maybe
Patrick Rothfuss' *Kingkiller Chronicle*, which I still think about.

I remember mentioning *The Wheel of Time* series in my [2021
retrospective](/blog/2021-in-review). I managed to read the first two,
but couldn't get into the third. Jordan's writing doesn't make for the
easiest of reading, and -- I speak for myself when I say this -- spacing
it out is probably best. Except I never got back.

This year, I'm hoping to read:

- more of *Dune*
- *The Doors of Stone* please dear God
- some more *Wheel of Time*, I think I've taken a long enough break
- *The Lost Metal*, despite not enjoying Era 2 as much

## this site

Reject modernity, embrace tradition -- only the one tradition where we
talk about this site and count the number of blog posts I wrote!

```
grep 'date: 2022' pages/blog/*.md | wc -l
8
```

Lowest yet, and the trend year-over-year doesn't look promising. I don't
think I'll ever *completely* stop writing, but I certainly won't be
writing as much as I used to. I've largely stopped writing "commentary"
since it's pretty pointless and inherently tied to the news cycle --
it loses readability value even just a month later.

## miscellaneous

The catch-all. The flytrap. The part where everything else too small to
deserve its own subsection get fleeting mentions. Let's run through them
real quick since I'm losing patience and the date on this blog post has
been changed four times already.

**The bullet journal**: I [wrote about this](/blog/bujo) in '21. While
the method largely remains the same, the size of my notebook has
decreased to A6, drawing inspiration from one of [my favourite articles
on note taking](https://ratfactor.com/notes). The smaller size allows me
to carry it around pretty easily, and the thinness lets me clip my
ball-pen at the current page.

![bujo](https://cdn.icyphox.sh/WtFWq.jpeg)

**Watches**: My (second) new expensive hobby. I went down the rabbithole
of [HMT](https://en.wikipedia.org/wiki/HMT_Limited)[^2] watches and
instantly fell in love. I'll admit HMT watches aren't *that* expensive,
but I've been looking at some Seikos and Hamiltons that I'd like to buy
this year.

![hmt jhalak](https://cdn.icyphox.sh/X17~Q.webp)

[^2]: Also see [r/hmtwatches](https://old.reddit.com/r/hmtwatches)

**Podcasts**: Made some great podcast discoveries last year:
- [Our Fake History](https://ourfakehistory.com/): deep dives into
  historical hoaxes
- [How to Get on a
  Watchlist](https://encyclopediageopolitica.com/how-to-get-on-a-watchlist/):
  experts discuss dangerous activities
- [Off Menu](https://www.offmenupodcast.co.uk/): Ed Gamble and James
  Acaster run an imaginary restaurant
- [The Russian Empire History
  Podcast](https://therussianempirehistorypodcast.com/): what it says on
  the tin

## in 2023...

There's a lot that happened last year, and there's *a whole lot more*
that's going to happen this year -- and very soon. I've been hinting at
it for a while on the [fedi](https://h.icyphox.sh/@icy). I've been
packing a whole lot for it, and it's a mere 4 days away as I write this.
It's a massive life update that I'm beyond stoked about -- I'll write
about it here in few days.

Until then, thanks for sticking around and I'll see you in a jiff.
