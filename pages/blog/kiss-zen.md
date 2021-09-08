---
template:
slug: kiss-zen
title: The Zen of KISS Linux
subtitle: My thoughts on the distro, the philosophy and my experience in general
date: 2020-04-03
---

[I installed KISS](/blog/five-days-tty) early in January on my main
machine -- an HP Envy 13 (2017), and I have since noticed a lot of changes
in my workflow, my approach to software (and its development), and in
life as a whole. I wouldn't call KISS "life changing", as that would be
overly dramatic, but it has definitely reshaped my outlook towards
technology -- for better or worse.

When I talk about KISS to people -- online or IRL -- I get some pretty
interesting reactions and comments.[^bringing-up-kiss] 
Ranging from "Oh cool." to "You must be
retarded.", I've heard it all. A classic and a personal favourite of
mine, "I don't use meme distros because I actually get work done." It is
actually, quite the opposite -- I've been so much more productive using
KISS than any other operating system. I'll explain why shortly.

[^bringing-up-kiss]: No, I don't go "I use KISS btw". I don't bring it
    up unless provoked.

The beauty of this "distro", is it isn't much of a distribution at all.
There is no big team, no mailing lists, no infrastructure. The entire
setup is so loose, and this makes it very convenient to swap things out
for alternatives. The main (and potentially community) repos all reside
locally on your system. In the event that Dylan decides to call it
quits and switches to Windows, we can simply just bump versions
ourselves, locally! The [KISS Guidestones](https://k1ss.org/guidestones)
document is a good read.

In the subseqent paragraphs, I've laid out the different things about
KISS that stand out to me, and make using the system a lot more
enjoyable.

## the package system

Packaging for KISS has been delightful, to say the least. It takes me
about 2 mins to write and publish a new package. Here's the `radare2`
package, which I maintain, for example.

The `build` file (executable):

```sh
#!/bin/sh -e

./configure \
    --prefix=/usr

make
make DESTDIR="$1" install
```

The `version` file:
```
4.3.1 1
```

The `checksums` file (generated using `kiss checksum radare2`):
```
4abcb9c9dff24eab44d64d392e115ae774ab1ad90d04f2c983d96d7d7f9476aa  4.3.1.tar.gz
```

And finally, the `sources` file:
```
https://github.com/radareorg/radare2/archive/4.3.1.tar.gz
```

This is literally the bare minimum that you need to define a package.
There's also the `depends` file where you specify the dependencies for
your package.
`kiss` also generates a `manifests` file to track all the files and
directories that your package creates during installation, for their
removal, if and when that occurs. Now compare this process with any
other distribution's.

## the community

As far as I know, it mostly consists of the `#kisslinux` channel on
Freenode and the [r/kisslinux](https://old.reddit.com/r/kisslinux)
subreddit. It's not that big, but it's suprisingly active, and super
helpful. There have been some interested new KISS-related projects
too: [kiss-games](https://github.com/sdsddsd1/kiss-games) -- a repository
for, well, Linux games; [kiss-ppc64le](https://github.com/jedavies-dev/kiss-ppc64le)
and [kiss-aarch64](https://github.com/jedavies-dev/kiss-aarch64) -- KISS
Linux ports for PowerPC and ARM64 architectures; 
[wyvertux](https://github.com/wyvertux/wyvertux) -- an attempt at
a GNU-free Linux distribution, using KISS as a base; and tons more.

## the philosophy

Software today is far too complex. And its complexity is only growing.
Some might argue that this is inevitable, and it is in fact progress.
I disagree. Blindly adding layers and layers of abstraction (Docker,
modern web "apps") isn't progress. Look at the Linux desktop ecosystem
today, for example -- monstrosities like GNOME and KDE are a result of
this...new wave software engineering.

I see KISS as a symbol of defiance against this malformed notion. You
don't _need_ all the bloat these DEs ship with to have a usable system.
Agreed, it's a bit more effort to get up and running, but it is entirely
worth it. Think of it as a clean table -- feels good to sit down and work on,
doesn't it? 

Let's take my own experience, for example. One of the initial few
software I used to install on a new system was `dunst` -- a notification
daemon. Unfortunately, it depends on D-Bus, which is Poetterware; ergo,
not on KISS. However, using a system without notifications has been very
pleasant. Nothing to distract you while you're in the zone.

Another instance, again involving D-Bus (or not), is Bluetooth audio. As
it happens, my laptop's 3.5mm jack is rekt, and I need to use Bluetooth
for audio, if at all. Sadly, Bluetooth audio on Linux hard-depends on
D-Bus. Bluetooth stacks that don't rely on D-Bus do exist, like on Android, 
but porting them over to desktop is non-trivial. However, I used this to
my advantage and decided not to consume media on my laptop. This has
drastically boosted my productivity, since I literally cannot watch
YouTube even if I wanted to. My laptop is now strictly work-only.
If I do need to watch the occasional video / listen to music, I use my
phone. Compartmentalizing work and play to separate devices has worked
out pretty well for me.

I'm slowly noticing myself favor low-tech (or no-tech) solutions to
simple problems too. Like notetaking -- I've tried plaintext files, Vim
Wiki, Markdown, but nothing beats actually using pen and paper. Tech,
from what I can see, doesn't solve problems very effectively. In some
cases, it only causes more of them. I might write another post
discussing my thoughts on this in further detail. 

I'm not sure what I intended this post to be, but I'm pretty happy with
the mindspill. To conclude this already long monologue, let me clarify
one little thing y'all are probably thinking, "Okay man, are you
suggesting that we regress to the Dark Ages?". No, I'm not suggesting
that we regress, but rather, progress mindfully.
