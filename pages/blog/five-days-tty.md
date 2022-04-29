---
template:
title: Five days in a TTY
slug: five-days-tty
subtitle: I installed KISS Linux
date: 2020-01-13
---

This new semester has been pretty easy on me, so far. I hardly every
have any classes (again, so far), and I've a ton of free time on my
hands. This calls for -- yep -- a distro hop! 

## Why KISS?

[KISS](https://getkiss.org) has been making rounds on the interwebz lately.[^hn]
The Hacker News post spurred _quite_ the discussion. But then again,
that is to be expected from Valleybros who use macOS all day. :^)

From the website,

> An independent Linux® distribution with a focus on simplicity and the
> concept of “less is more”. The distribution targets *only* the x86-64
> architecture and the English language.

Like many people did in the HN thread, "simplicity" here is not to be
confused with "ease". It is instead, simplicity in terms of lesser and
cleaner code -- no
[Poetterware](https://www.urbandictionary.com/define.php?term=poetterware).

[^hn]: https://news.ycombinator.com/item?id=21021396

This, I can get behind. A clean system with less code is like a clean
table. It's nice to work on. It also implies security to a certain
extent since there's a smaller attack surface. 

The [`kiss`](https://github.com/kisslinux/kiss) package manager is written
is pure POSIX sh, and does _just enough_. Packages are compiled from
source and `kiss` automatically performs dependency resolution. Creating
packages is ridiculously easy too.

Speaking of packages, all packages -- both official & community
repos -- are run through `shellcheck` before getting merged. This is
awesome; I don't think this is done in any other distro.

In essence, KISS sucks less.

## Installing KISS

The [install guide](https://getkiss.org/pages/install) is very easy to
follow. Clear instructions that make it hard to screw up; that didn't
stop me from doing so, however.

### Day 1

Although technically not in a TTY, it was still not _in_ the KISS
system -- I'll count it. I'd compiled the kernel in the chroot and
decided to use `efibootmgr` instead of GRUB. `efibootmgr` is a neat tool
to modify the Intel Extensible Firmware Interface (EFI). Essentially,
you boot the `.efi` directly as opposed to choosing which boot entry
you want to boot, through GRUB. Useful if you have just one OS on the
system. Removes one layer of abstraction.

Adding a new EFI entry is pretty easy. For me, the command was:

```
efibootmgr --create 
           --disk /dev/nvme0n1 \
           --part 1 \
           --label KISS Linux \
           --loader /vmlinuz
           --unicode 'root=/dev/nvme0n1p3 rw'  # kernel parameters
```

Mind you, this didn't work the first time, or the second, or the
third ... a bunch of trial and error (and asking on `#kisslinux`)
later, it worked.

Well, it booted, but not into KISS. Took a while to figure out that the
culprit was `CONFIG_BLK_DEV_NVME` not having been set in the kernel
config. Rebuild & reboot later, I was in.

### Day 2

Networking! How fun. An `ip a` and I see that both USB tethering
(ethernet) and wireless don't work. Great. Dug around a bit -- missing
wireless drivers was the problem. Found my driver, a binary `.ucode` from
Intel (eugh!). The whole day was spent in figuring out why the kernel
would never load the firmware. I tried different variations -- loading
it as a module (`=m`), baking it in (`=y`) but no luck.

### Day 3

I then tried Alpine's kernel config but that was so huge and had a _ton_
of modules and took far too long to build each time, much to my
annoyance. Diffing their config and mine was about ~3000 lines! Too much
to sift through. On a whim, I decided to scrap my entire KISS install
and start afresh. 

For some odd reason, after doing the _exact_ same things I'd done
earlier, my wireless worked this time. Ethernet didn't, and still
doesn't, but that's ok.

Building `xorg-server` was next, which took about an hour, mostly thanks
to spotty internet. The build went through fine, though what wasn't was
no input after starting X. Adding my user to the `input` group wasn't
enough. The culprit this time was a missing `xf86-xorg-input` package.
Installing that gave me my mouse back, but not the keyboard!

It was definitely not the kernel this time, because I had a working
keyboard in the TTY. 

### Day 4 & Day 5

This was probably the most annoying of all, since the fix was _trivial_.
By this point I had exhausted all ideas, so I decided to build my
essential packages and setup my system. Building Firefox took nearly
9 hours, the other stuff were much faster.

I was still chatting on IRC during this, trying to zero down on what the
problem could be. And then:

```
<dylanaraps> For starters I think st fails due to no fonts.
```

Holy shit! Fonts. I hadn't installed _any_ fonts. Which is why none of
the applications I tried launching via `sowm` ever launched, and hence,
I was lead to believe my keyboard was dead.

## Worth it?

Absolutely. I _cannot_ stress on how much of a learning experience this
was. Also a test of my patience and perseverance, but yeah ok. I also
think that this distro is my endgame (yeah, right), probably because
other distros will be nothing short of disappointing, in one way or
another.

Huge thanks to the folks at `#kisslinux` on Freenode for helping me
throughout. And I mean, they _really_ did. We chatted for hours on end
trying to debug my issues.

I'll now conclude with an obligatory screenshot.

![scrot](https://cdn.icyphox.sh/R6G.png)
