---
template: page.html
title: uses
subtitle: Hardware and software that I use.
---

I often get asked about my computing setup -- my computers, the software
I run on them, how I host my services, and other choices of personal
technology. This is a relatively up-to-date list detailing what I'm
currently using.

## personal laptop (lapis)

My primary laptop that I use for everything non-work is my [**Asus ROG
Flow X13 (2021)**](/blog/flow-x13). It's got a Ryzen 9 5900HS, Nvidia
GTX 1650 Max-Q, 32GB of RAM and a 1TB SSD. I bought this machine in
early 2022, when I was working remotely as a contractor. The 4K display
doesn't help with its battery life (about 7 hours) but it looks
absolutely fantastic.

![flow x13 at oodi](https://cdn.icyphox.sh/w6UH4.jpg)

This laptop currently runs NixOS. I would ideally like to run OpenBSD,
but I figured I'd make use of its GPU for the occasional game and run
Linux instead; NixOS just seemed like the least-shit choice. I like its
declarative approach to system configuration, but I won't pretend -- I'd
have much preferred a more sane language like Lua.

Other software I use on this machine:

- **KDE Plasma**: It's been alright as a desktop environment but I only
  care to use it for Wayland and I don't have time to dick around with a
  window manager. But that might change.

- **tmux**: Most of my actual "window" management happens here. I have
  it
  [configured](https://git.icyphox.sh/dotfiles/blob/master/nix/programs/tmux.nix)
  to show my current working directory and git info in the statusline --
  this helps me keep my actual prompt clean and quick.

- **neovim**: My editor of choice. I made the switch to the famously
  awaited 0.5.0 branch that introduced Lua support [very
  early](/blog/nvim-lua/) and haven't looked back since. I use a [custom
  duotone
  colorscheme](https://git.icyphox.sh/dotfiles/blob/master/config/nvim/colors/plain.vim).

- **QtPass**: Frontend for passwords managed using GPG.

- **Firefox**: It works; not much else to say. These are the add-ons I
  use:
  * Don't F* with Paste: for those pesky bank logins that block paste in
    the password fields
  * Refined Hacker News
  * Sidebery: tab-tree on the left
  * Simple Translate: for Finnish/Russian
  * SponsorBlock
  * uBlock Origin
  * Web Scrobbler
  * Multi-Account Containers

## work laptop (kvothe)

For work, I use a **14" M1 MacBook Pro**. I use
[nix-darwin](https://github.com/LnL7/nix-darwin) to configure most of my
basic applications (neovim, tmux, bash, ...). Software of note:

- **iTerm2**: I don't use 90% of its features but I like that it lets me
  cofigure terminal padding. I prefer to run a single instance of iTerm,
  full-screened and without any borders. I use tmux for everything else.

- **Rectangle**: For the occasional window management.

## home server (denna)

![denna under the table](https://cdn.icyphox.sh/fxIFy.jpg)

My latest addition. I bought this HP EliteDesk on
[Tori.fi](https://tori.fi) for a princely sum of 60 EUR. It has an i5
6500, 8GB of RAM and a 500GB HDD. I installed OpenBSD on it at work by
wiring it up to a monitor using DisplayPort (it does not have HDMI).
It now runs very quitely under my table, plugged into the router.

I didn't feel like paying my ISP for a static IP and since I work for a
[cloud provider](https://upcloud.com), I spun up a VPS with a public IP
and setup a quick Nginx TCP proxy to forward traffic to my home server.

```conf
stream {
        server {
                listen 80;
                listen [::]:80;
                proxy_pass denna:80;
        }
        server {
                listen 443;
                listen [::]:443;
                proxy_pass denna:443;
        }
}
```

Then, using [httpd(8)](https://man.openbsd.org/httpd.8) and
[relayd(8)](https://man.openbsd.org/relayd.8) I run a few services (with
more to come):

- This website.
- [legit](https://git.icyphox.sh/legit): Web frontend for git, written
  in Go.
- [honk](https://h.icyphox.sh): ActivityPub server.
- [fsrv](https://git.icyphox.sh/fsrv): File hosting and upload server,
  written in Go.
- [radicale](https://radicale.org): Contacts and calendar (Cal/CardDav)
  server.

## other technology

Some hardware and software that are in frequent use across all my
devices:

- **Ferricy**: 34-key wireless split keyboard designed by me, based on
  the Ferris Sweep. I have both the MX (Gazzew Boba LT switches) and the
  Choc (Kailh Sunset switches) variants, but I find myself favoring the
  low actuation force of the MX one more. Some [pictures
  here](/blog/2022-in-review/#keyboards-my-first-new-expensive-hobby).

- **Logitech Ergo M575**: Wireless ergonomic thumb trackball mouse. I've
  [written about it](/blog/m575) in depth.

- **realme Buds Air 3s**: El-cheapo truly-wireless earphones. They look
  pretty slick, and fit very comfortably. I mostly use them at the gym
  or while commuting in the metro.

- **iPhone 13 mini**: It's unfortunate that I have to use an Apple
  device but it's also the only real small phone in the market. I quite
  enjoy how it fits in my palm, and being able to reach the top of the
  screen with one hand. I plan to stick to this until Apple stops
  updating it.

- **Kindle KT4**: Jailbroken using
  [WatchThis](https://www.mobileread.com/forums/showthread.php?t=346037)
  and running KOReader.

- **Tailscale**: I used to setup WireGuard networks by hand, but that
  got unweildy after 3 hosts. With Tailscale I now have around 8
  different machines running Linux, OpenBSD, macOS and iOS all
  seamlessly connected. It's incredibly handy.

- **Migadu**: I too, like everyone else, gave up on self-hosting my
  email. Migadu is very straightforward, and very cheap (19 EUR/year).
  Works great with all my email clients.
