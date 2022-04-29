---
template:
slug: pi
title: Migrating to the RPi
subtitle: Raspberry Pi shenanigans, and other things
date: 2020-06-04
---

I'd ordered the Raspberry Pi 4B (the 4GB variant), sometime early
this year, thinking I'd get to self-hosting everything on it as soon as
it arrived. As things turn out, it ended up sitting in its box up until
two weeks ago -- it took me _that_ long to order an SD card for it. No,
I didn't have one. Anyway, from there began quite the wild ride.

## flashing the SD card

You'd think this would be easy right? Just plug it into your laptop's SD
card reader (or microSD), and flash it like you would a USB drive. Well,
nope. Of the three laptops at home one doesn't have an SD card reader,
mine -- running OpenBSD -- didn't detect it, and my brother's -- running
Void -- didn't detect it either. 
 
Then it hit me: my phone (my brother's, actually), has an SD card slot
that actually works. Perhaps I can use the phone to flash the image?
Took a bit of DDG'ing (ducking?), but we eventually figured out that the
block-device for the SD on the phone was `/dev/mmcblk1`. Writing to it
was just the usual `dd` invocation.

## got NAT'd

After the initial setup, I was eager to move my services off the Digital
Ocean VPS, to the RPi. I set up the SSH port forward through my router
config, as a test. Turns out my ISP has me NAT'd. The entirety of my
apartment is serviced by these fellas, and they have us all under
a CG-NAT. Fantastic.

Evading this means I either lease a public IP from the ISP, or
I continue using my VPS, and port forward traffic from it via a tunnel.
I went with option two since it gives me something to do.

## NAT evasion

This was fairly simple to setup with Wireguard and `iptables`. I don't
really want to get into detail here, since it's been documented aplenty
online, but in essence you put your VPS and the Pi on the same network,
and forward traffic hitting your internet facing interface (`eth0`) 
to the VPN's (`wg0`). Fairly simple stuff.

## setting up Mastodon on the Pi

Mastodon was kind of annoying to get working. My initial plan was to
port forward only a few selected ports, have Mastodon exposed on the Pi
at some port via nginx, and then front _that_ nginx via the VPS. So
basically: Mastodon (localhost on Pi) <-> nginx (on Pi) <-> nginx (on
VPS, via Wireguard). I hope that made sense.

Anyway, this setup would require having Mastodon run on HTTP, since I'll
be HTTPS'ing at the VPS. If you think about it, it's kinda like what
Cloudflare does. But, Mastodon doesn't like running on HTTP. It just
wasn't working. So I went all in and decided to forward all 80/443
traffic and serve everything off the Pi.

Getting back to Mastodon -- the initial few hiccups aside, I was able to
get it running at `toot.icyphox.sh`. However, as a seeker of aesthetics,
I wanted my handle to be `@icyphox.sh`. Turns out, this can be achieved
fairly easily. 

Add a new `WEB_DOMAIN` variable to your `.env.production` file, found in
your Mastodon root dir. Set `WEB_DOMAIN` to your desired domain, and
`LOCAL_DOMAIN` to the, well, undesired one. In my case:

    WEB_DOMAIN=icyphox.sh
    LOCAL_DOMAIN=toot.icyphox.sh

Funnily enough, the 
[official documentation for this](https://github.com/tootsuite/documentation/blob/archive/Running-Mastodon/Serving_a_different_domain.md)
says the exact opposite, which...doesn't work.

I don't really understand, but whatever it works and now my Mastodon is
@[x@icyphox.sh](https://toot.icyphox.sh/@x). I'm not complaining. Send
mail if you know what's going on here.

And oh, here's the protective case [nerd](https://peppe.rs) fashioned
out of cardboard.

![](https://cdn.icyphox.sh/zn2I3.jpg)
