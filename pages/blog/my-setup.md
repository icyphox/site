---
template: text.html
title: My setup
subtitle: My daily drivers—hardware, software and workflow
date: 2019-05-13
slug: my-setup
---

**Update**: I now maintain a [uses](/uses) page. This post is out of
date.

## Hardware

The only computer I have with me is my [HP Envy 13
(2018)](https://store.hp.com/us/en/mdp/laptops/envy-13) (my model looks
a little different). It’s a 13” ultrabook, with an i5 8250u, 8 gigs of
RAM and a 256 GB NVMe SSD. It’s a very comfy machine that does
everything I need it to.

For my phone, I use a [OnePlus 6T](https://www.oneplus.in/6t), running
stock [OxygenOS](https://www.oneplus.in/oxygenos). As of this writing,
its bootloader hasn’t been unlocked and nor has the device been rooted.
I’m also a proud owner of a [Nexus
5](https://en.wikipedia.org/wiki/Nexus_5), which I really wish Google
rebooted. It’s surprisingly still usable and runs Android Pie, although
the SIM slot is ruined and the battery backup is abysmal.

My watch is a [Samsung Gear S3
Frontier](https://www.samsung.com/in/wearables/gear-s3-frontier-r760/).
Tizen is definitely better than Android Wear.

My keyboard, although not with me in college, is a very old [Dell
SK-8110](https://www.amazon.com/Dell-Keyboard-Model-SK-8110-Interface/dp/B00366HMMO).
For the little bit of gaming that I do, I use a [HP
m150](https://www.hpshopping.in/hp-m150-gaming-mouse-3dr63pa.html)
gaming mouse. It’s the perfect size (and color).

For my music, I use the [Bose SoundLink
II](https://www.boseindia.com/en_in/products/headphones/over_ear_headphones/soundlink-around-ear-wireless-headphones-ii.html).
Great pair of headphones, although the ear cups need replacing.

## And the software

<del>My distro of choice for the past ~1 year has been [elementary
OS](https://elementary.io). I used to be an Arch Linux elitist, complete
with an esoteric window manager, all riced. I now use whatever
JustWorks™.</del>

**Update**: As of June 2019, I've switched over to a vanilla Debian
9 Stretch install, running [i3](https://i3wm.org) as my window manager.
If you want, you can dig through my configs at my
[dotfiles](https://github.com/icyphox/dotfiles) repo. 

Here’s a (riced) screenshot of my desktop. 

![scrot](https://i.redd.it/jk574gworp331.png)

Most of my work is done in either the browser, or the terminal. My shell
is pure [zsh](http://www.zsh.org), as in no plugin frameworks. It’s
customized using built-in zsh functions. Yes, you don’t actually need
a framework. It’s useless bloat. The prompt itself is generated using
a framework I built in [Nim](https://nim-lang.org) --
[nicy](https://github.com/icyphox/nicy). My primary text editor is
[nvim](https://neovim.org). Again, all configs in my dotfiles repo
linked above. I manage all my passwords using
[pass(1)](https://passwordstore.org), and I use
[rofi-pass](https://github.com/carnager/rofi-pass) to access them via
`rofi`.

Most of my security tooling is typically run via a Kali Linux docker
container. This is convenient for many reasons, keeps your global
namespace clean and a single command to drop into a Kali shell.

I use a DigitalOcean droplet (BLR1) as a public filehost, found at
[cdn.icyphox.sh](https://cdn.icyphox.sh). The UI is the wonderful
[serve](https://github.com/zeit/serve), by [ZEIT](https://zeit.co). The
same box also serves as my IRC bouncer and OpenVPN (TCP), which I tunnel
via SSH running on 443. Campus firewall woes. 

I plan on converting my desktop back at home into a homeserver setup.
pSoon™.
