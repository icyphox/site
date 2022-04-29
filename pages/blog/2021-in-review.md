---
template:
slug: 2021-in-review
title: 2021 in review
subtitle: The post-year ramble is here, slightly late this time
date: 2022-01-10
---

The last year was quite eventful to say the least, and I'd been putting
off on writing this retrospective simply because of the sheer number of
things that happened/I did, of varying levels of importance -- both to
you as a reader, and me as... well, the one who experienced them. 

I'll try to highlight the major ones here -- they're also the ones I'm
okay to discuss publicly, so there's that. As for the rest: they'll
serve as conversation fuel for 2022.

## I graduated... barely

After 4 long years, mostly "learning" about things that haven't been
used since like, my mom was born (I'm looking at you Intel 8086), I am
now a Bachelor of Technology in Computer Science and Engineering. I say
barely because I actually did pretty terribly. I'm still mildly
surprised that given my GPA, the degree certificate classifies it as a
"First Class". I think they just felt sorry for us lot.

Was it a waste of time? A lot of the coursework, sadly, was. But my time
in college -- however little -- was actually quite fun. One thing's for
sure: I can't rewind time to see what would've happened had I _not_ done
the degree; but now I've done it, and here we are. Wherever that is.
Maybe it helped, maybe it didn't. Oh well.

## my time at DeepSource

This time last year (January 2021), I joined
[DeepSource](https://deepsource.io) as a Security Engineer (SRE on
paper). Suffice to say, I had an excellent time there, working with some
equally excellent people. I got to touch a whole bunch of systems:
ranging from observability pipelines, mesh networks in Kubernetes,
cloud-native security, and some more Kubernetes.

Oh, and here are a few pictures from our trip to the Maldives.[^1]

![maldives 1](https://cdn.icyphox.sh/FX~bI.jpg)
![maldives 2](https://cdn.icyphox.sh/DMHDG.jpg)

[^1]:  If you're in Bangalore and are looking for work, definitely
    consider [applying to DeepSource](https://careers.deepsource.io)!

In December 2021, I decided to leave DeepSource in favor of other
opportunities. I must say, I will deeply miss my equity when DeepSource
eventually becomes a unicorn -- and I'm confident they will! As for the
other opportunities, I will write about that in a future post. This is a
_retrospective_ after all.[^2]

[^2]: There are hints... in various places...

## projects and hacks

Probably my biggest and most fun project this year was
[forlater.email](https://forlater.email). Both the site, and its
[technical breakdown](/blog/building-forlater) frontpaged on Hacker News
and was pretty well received. In hindsight, I should've included some
kind of payment model, but at the same time, being flexible enough to
accomodate those that can't afford to pay. And the code is shit. I'll
probably rewrite it. Eventually.[^3]

[^3]: Sure, lol.

My attempt at running [Kubernetes at home](/blog/k8s-at-home), while
being super fun, failed miserably. I learnt a ton from it however, and I
have no regrets. Setting up a Wireguard mesh manually, bootstrapping a
cluster using `kubeadm`, multi-arch considerations, etc. I do sorely
miss the declarative-ness of it all, I must say.

Besides these, I don't think I spent any serious amount of time on
anything else. Other than, of course, work projects.

## this site

As is tradition, let's talk about this site and the blog. There have
been some minor visual changes but I think it's largely stayed the same.
I've found the aesthetic I like -- at least for now.

I've re-added the [reading](/reading) page to publicly track books that
I've read. More on that in a bit.

As for blog posts this year, let's see:

```console
$ grep 'date: 2021' pages/blog/*.md | wc -l
      13
```

Only 13! That's about 1 a month, and the lowest count per year so far.
I'll attribute this to me dedicating more time to work, i.e. I've become
a wagie cagie. Make of that what you will. That said, I think the
quality of posts has considerably increased. I think.

## other stuff

I couldn't think of an appropriate heading for this section so "other
stuff" it is: a catch-all category for general life-ey things.

I read a grand-total of 9 books last year -- not particularly good. I'd
like to at least double that this year. Some of my favourite reads were:
_Dune_, _The Hero of Ages_, _The Enemy_ and _Permanent Record_. Big
thanks to [Vishesh](https://awalvie.me) for _Dune_ and
[Vishnu](https://twitter.com/thebluefowl) for _Permanent Record_!

Language learning took an unfortunate hit, with basically zero progress
in Russian. I did study it for a month or two in early 2021, but I won't
count it for I've likely forgotten it all. I hope to restart where I
left off, this year -- hopefully with the help of my new [productivity
hacks](/blog/bujo) (which has been working wonders, by the way!).

I had roughly about 6 - 7 months of time to hit the gym, i.e. when the
gym wasn't closed off, and I managed to get some swole on. As of this
writing, it's the "third wave" of COVID-19 and the gym's closed. Again.

In other somewhat big news: I switched to an iPhone 13 mini. This
probably warrants its own big post -- one full of copes and hopes. I
will have to mull over it a bit to fully articulate my thoughts. I have
a few other post ideas as well -- many that I planned on writing last
year but never got around to. I often consider writing commentary on
`$TECH_OUTRAGE_DU_JOUR` but everything that I want to say has usually
already been said. I'm sure there'll be plenty of stuff I can be the
_first_ to comment on in 2022.

And speaking of 2022...

## 2022 might be big

This might be a big year for me, with some potentially huge life
updates. New job, new adventures, the works. I'm looking forward to it.
2021 was super eventful; 2022 just might top it.

Here's a list of things I'm looking forward to this year:

- Formula 1: New regulations! Williams back on top? Who knows?!
- New albums: Oceans Ate Alaska, I See Stars (one can hope!), Invent
  Animate.
- Travel.
- Reading _The Wheel of Time_ series.

I'm going to close off this rambly post with a big thanks to everyone who's
supporting forlater.email -- it made my whole last year. Maybe this year
too. And you just might see another micro-SaaS from me!

I'll see you soon.
