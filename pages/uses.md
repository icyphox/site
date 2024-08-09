---
template: page.html
title: uses
subtitle: Hardware and software that I use.
---

I often get asked about my computing setup -- my computers, the software
I run on them, how I host my services, and other choices of personal
technology. This is a relatively up-to-date list detailing what I'm
currently using.

## personal laptop (wyndle)

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

- **GNOME**: I'm liking it a ton more than KDE Plasma. Especially love
  the trackpad gestures and general feel of the UI.

- **tmux**: Most of my actual "window" management happens here. I have
  it
  [configured](https://git.icyphox.sh/dotfiles/blob/master/programs/tmux.nix)
  to show my current working directory and git info in the statusline --
  this helps me keep my actual prompt clean and quick.

- **neovim**: My editor of choice. I made the switch to the famously
  awaited 0.5.0 branch that introduced Lua support [very
  early](/blog/nvim-lua/) and haven't looked back since. I use a [custom
  duotone
  colorscheme](https://git.icyphox.sh/dotfiles/blob/master/nvim/colors/plain.lua).

- **Zed**: I've been dailying Zed for while now and it has replaced
  Neovim for most of my editing tasks scoped to projects. I still reach
  for Neovim for one-off edits in the terminal.

- **Bitwarden**: I run a Vaultwarden server in my homelab K3s cluster
  and use the official Bitwarden clients everywhere else.


## work laptop (kvothe)

For work, I use a **14" M1 MacBook Pro**. I use
[nix-darwin](https://github.com/LnL7/nix-darwin) to configure most of my
basic applications (neovim, tmux, bash, ...). Software of note:

- **alacritty**: Much faster than iTerm and a whole bunch lighter. And I
can configure it using Nix!

- **Raycast**: Launcher and window management.

- **Orion**: Safari but better.

## homelab k3s cluster

3-node K3s cluster:
- sini: 8GB, i5-6500T, 256GB SSD
- iso: 8GB, i5-6500, 500GB HDD
- denna: 8GB, N100, 128GB eMMC

More info at [git.icyphox.sh/infra](https://git.icyphox.sh/infra).

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

- **Airpods Pro**: Great quality, even better noise cancellation.

- **iPhone 13 mini**: It's unfortunate that I have to use an Apple
  device but it's also the only real small phone in the market. I quite
  enjoy how it fits in my palm, and being able to reach the top of the
  screen with one hand. I plan to stick to this until Apple stops
  updating it.

- **Kindle KT4**: Jailbroken using
  [WatchThis](https://www.mobileread.com/forums/showthread.php?t=346037)
  and running KOReader.

- **iPhone 15 Pro**: "Work" phone. Not a fan of its size, but I love the
  refresh rate. This is currently my main phone.

- **Tailscale**: I used to setup WireGuard networks by hand, but that
  got unweildy after 3 hosts. With Tailscale I now have around 8
  different machines running Linux, OpenBSD, macOS and iOS all
  seamlessly connected. It's incredibly handy.
