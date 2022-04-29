---
template:
slug: openbsd-hp-envy
title: OpenBSD on the HP Envy 13
subtitle: I put a blowfish in my laptop this week
date: 2020-04-17
---

My existing KISS install broke because I thought it would be a great
idea to have [apk-tools](https://github.com/alpinelinux/apk-tools)
alongside the `kiss` package manager. It's safe to say, that did not end
well -- especially when I installed, and then removed a package. With
a semi-broken install that I didn't feel like fixing, I figured I'd give
OpenBSD a try. And I did.

## installation and setup

Ran into some trouble booting off the USB initially, turned out to be
a faulty stick. Those things aren't built to last, sadly. Flashed a new
stick, booted up. Setup was pleasant, very straightforward. Didn't
really have to intervene much.

After booting in, I was greeted with a very archaic looking FVWM
desktop. It's not the prettiest thing, and especially annoying to work
with when you don't have your mouse setup, i.e. no tap-to-click. 

I needed wireless, and my laptop doesn't have an Ethernet port. USB
tethering just works, but the connection kept dying. I'm not sure why.
Instead, I downloaded the [iwm(4)](http://man.openbsd.org/iwm.4)
firmware from [here](http://firmware.openbsd.org/firmware/6.6/), loaded
it up on a USB stick and copied it over to `/etc/firmware`. After that,
it was as simple as running
[fw_update(1)](http://man.openbsd.org/fw_update.1)
and the firmware is auto-detected and loaded. In fact, if you have working 
Internet, `fw_update` will download the required firmware for you, too.

Configuring wireless is painless and I'm so glad to see that there's no
`wpa_supplicant` horror to deal with. It's as simple as:

```
$ doas ifconfig iwm0 nwid YOUR_SSID wpakey YOUR_PSK
```

Also see [hostname.if(5)](http://man.openbsd.org/hostname.if.5) to make
this persist. After that, it's only a matter of specifying your desired
SSID, and `ifconfig` will automatically auth and procure an IP lease.

```
$ doas ifconfig iwm0 nwid YOUR_SSID
```

By now I was really starting to get exasperated by FVWM, and decided to
switch to something nicer. I tried building 2bwm (my previous WM), but
that failed. I didn't bother trying to figure this out, so I figured I'd
give [cwm(1)](http://man.openbsd.org/cwm.1) a shot. Afterall, people
sing high praises of it.

And boy, is it good. The config is a breeze, and actually pretty
powerful. [Here's mine](https://github.com/icyphox/dotfiles/blob/master/home/.cwmrc).
cwm also has a built-in launcher, so dmenu isn't necessary anymore.
Refer to [cwmrc(5)](https://man.openbsd.org/cwmrc.5) for all the config
options.

Touchpad was pretty simple to setup too -- OpenBSD has
[wsconsctl(8)](http://man.openbsd.org/wsconsctl.8), which lets you set
your tap-to-click, mouse acceleration etc. However, more advanced
configuration can be achieved by getting Xorg to use the Synaptics
driver. Just add a `70-synaptics.conf` to `/etc/X11/xorg.conf.d` (make
the dir if it doesn't exist), containing:

```conf
Section "InputClass"
	Identifier "touchpad catchall"
	Driver "synaptics"
	MatchIsTouchpad "on"
    Option "TapButton1" "1"
    Option "TapButton2" "3"
    Option "TapButton3" "2"
    Option "VertEdgeScroll" "on"
    Option "VertTwoFingerScroll" "on"
    Option "HorizEdgeScroll" "on"
    Option "HorizTwoFingerScroll" "on"
	Option "VertScrollDelta" "111"
	Option "HorizScrollDelta" "111"
EndSection	
```

There are a lot more options that can be configured, see
[synaptics(4)](http://man.openbsd.org/synaptics.4).

Suspend and hibernate just work, thanks to
[apm(8)](http://man.openbsd.org/apm.8). Suspend on lid-close just needs
one `sysctl` tweak:

```
$ sysctl machdep.lidaction=1
```

I believe it's set to 1 by default on some installs, but I'm not sure.

## impressions

I already really like the philosophy of OpenBSD -- security and
simplicity, while not losing out on sanity. The default install is
plentiful, and has just about everything you'd need to get going. 
I especially enjoy how everything just works! I was pleasantly surprised
to see my brightness and volume keys work without any configuration!
It's clear that the devs
actually dogfood OpenBSD, unlike uh, *cough* Free- *cough*. Gosh I hope
it's not _the_ flu. :^)

Oh and did you notice all the manpage links I've littered throughout
this post? They have manpages for _everything_; it's ridiculous. And
they're very thorough. Arch Wiki is good, but it's incorrect at times,
or simply outdated. OpenBSD's manpages, although catering only to
OpenBSD have never failed me. 

Performance and battery life are fine. Battery is in fact, identical, if
not better than on Linux. OpenBSD disables HyperThreading/SMT for
security reasons, but you can manually enable it if you wish to do so:

```
$ sysctl hw.smt=1
```

Package management is probably the only place where OpenBSD falls short. 
[pkg_add(1)](http://man.openbsd.org/pkg_add.1) isn't particularly fast,
considering it's written in Perl. The ports selection is fine, I have
yet to find something that I need not on there. I also wish they
debloated packages; maybe I've just been spoilt by KISS. I now have
D-Bus on my system thanks to Firefox. :(

I appreciate the fact that they don't have a political document -- a Code
of Conduct. CoCs are awful, and have only proven to be harmful for
projects; part of the reason why I'm sick of Linux and its community.
Oh wait, OpenBSD does have one: https://www.openbsd.org/mail.html
;)

I'll be exploring [vmd(8)](http://man.openbsd.org/vmd.8) to see if I can
get a Linux environment going. Perhaps that'll be my next post, but when
have I ever delivered?

I'll close this post off with my new rice, and a sick ASCII art I made.

```
      \. -- --./  
      / ^ ^ ^ \
    (o)(o) ^ ^ |_/|
     {} ^ ^ > ^| \|
      \^ ^ ^ ^/
       / -- --\
                    ~icy
```

![openbsd rice](https://cdn.icyphox.sh/zDYdj.png)
