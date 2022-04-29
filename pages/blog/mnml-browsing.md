---
template:
title: Vimb&#58; my Firefox replacement
subtitle: Web browsing, suckless style
date: 2020-01-16
slug: mnml-browsing
---


After having recently installed [KISS](https://getkiss.org), and
building Firefox from source, I was exposed to the true monstrosity that
Firefox -- and web browsers in general -- is. It took all of 9 hours to
build the dependencies and then Firefox itself.

Sure, KISS now ships Firefox binaries in the
[firefox-bin](https://github.com/kisslinux/repo/tree/master/extra/firefox-bin)
package; I decided to get rid of that slow mess anyway.

## Enter vimb

[vimb](https://fanglingsu.github.io/vimb/) is a browser based on
[webkit2gtk](https://webkitgtk.org/), with a Vim-like interface. 
`webkit2gtk` builds in less than a minute -- it blows Firefox out of
the water, on that front.

There isn't much of a UI to it -- if you've used Vimperator/Pentadactyl
(Firefox plugins), vimb should look familiar to you.
It can be configured via a `config.h` or a text based config file at
`~/.config/vimb/config`.
Each "tab" opens a new instance of vimb, in a new window but this can
get messy really fast if you have a lot of tabs open.

## Enter tabbed

[tabbed](https://tools.suckless.org/tabbed/) is a tool to _embed_ X apps
which support xembed into a tabbed UI. This can be used in conjunction
with vimb, like so:

```
tabbed vimb -e
```

Where the `-e` flag is populated with the `XID`, by tabbed. Configuring
Firefox-esque keybinds in tabbed's `config.h` is relatively easy. Once
that's done -- voilà! A fairly sane, Vim-like browsing experience that's
faster and has a smaller footprint than Firefox.

## Ad blocking

Ad blocking support isn't built-in and there is no plugin system
available. There are two options for ad blocking:

1. [wyebadblock](https://github.com/jun7/wyebadblock)
2. `/etc/hosts`

## Caveats

_Some_ websites tend to not work because they detect vimb as an older
version of Safari (same web engine). This is a minor inconvenience, and
not a dealbreaker for me. I also cannot login to Google's services for
some reason, which is mildly annoying, but it's good in a way -- I am now
further incentivised to dispose of my Google account.

And here's the screenshot y'all were waiting for:

![](https://cdn.icyphox.sh/d03i0.png)
