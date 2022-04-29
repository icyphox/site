---
template:
slug: prosody
title: Setting up Prosody for XMPP
subtitle: I setup Prosody yesterday—here's how I did it
date: 2020-02-18
---

Remember the [IRC for DMs](/blog/irc-for-dms/) article I wrote a while
back? Well...it's safe to say that IRC didn't hold up too well. It first
started with the bot. Buggy code, crashed a lot -- we eventually gave up
and didn't bring the bot back up. Then came the notifications, or lack
thereof. Revolution IRC has a bug where your custom notification rules
just get ignored after a while. In my case, this meant that
notifications for `#crimson` stopped entirely. Unless, of course, Nerdy
pinged me each time.

Again, none of these problems are inherent to IRC itself. IRC is
fantastic, but perhaps wasn't the best fit for our usecase. I still do
use IRC though, just not for 1-on-1 conversations.

## Why XMPP?

For one, it's better suited for 1-on-1 conversations. It also has
support for end-to-end encryption (via OMEMO), something IRC doesn't
have.[^otr] Also, it isn't centralized (think: email).

[^otr]: I'm told IRC supports OTR, but I haven't ever tried.

## So...Prosody

[Prosody](https://prosody.im) is an XMPP server. Why did I choose this
over ejabberd, OpenFire, etc.? No reason, really. Their website looked
cool, I guess.

### Installing

Setting it up was pretty painless (I've [experienced
worse](/blog/mailserver)). If you're on a Debian-derived system, add:
```
# modify according to your distro
deb https://packages.prosody.im/debian buster main 
```

to your `/etc/apt/sources.list`, and:

```
# apt update
# apt install prosody
```

### Configuring

Once installed, you will find the config file at
`/etc/prosody/prosody.cfg.lua`. Add your XMPP user (we will make this
later), to the `admins = {}` line.

```
admins = {"user@chat.example.com"}
```

Head to the `modules_enabled` section, and add this to it:

```
modules_enabled = {
    "posix";
    "omemo_all_access";
...
    -- uncomment these
    "groups";
    "mam";
    -- and any others you think you may need
}
```

We will install the `omemo_all_access` module later.

Set `c2s_require_encryption`, `s2s_require_encryption`, and
`s2s_secure_auth` to `true`.
Set the `pidfile` to `/tmp/prosody.pid` (or just leave it as default?).

By default, Prosody stores passwords in plain-text, so fix that by
setting `authentication` to `"internal_hashed"`

Head to the `VirtualHost` section, and add your vhost. Right above it,
set the path to the HTTPS certificate and key:

```
certificates = "certs"    -- relative to your config file location
https_certificate = "certs/chat.example.com.crt"
https_key = "certs/chat.example.com.key"
...

VirtualHost "chat.example.com"
```

I generated these certs using Let's Encrypt's `certbot`, you can use
whatever. Here's what I did:

```
# certbot --nginx -d chat.example.com
```

This generates certs at `/etc/letsencrypt/live/chat.example.com/`. You can
trivially import these certs into Prosody's `/etc/prosody/certs/` directory using:

```
# prosodyctl cert import /etc/letsencrypt/live/chat.example.com
```

### Plugins

All the modules for Prosody can be `hg clone`'d from
https://hg.prosody.im/prosody-modules. You will, obviously, need
Mercurial installed for this.

Clone it somewhere, and: 

```
# cp -R prosody-modules/mod_omemo_all_access /usr/lib/prosody/modules
```

Do the same thing for whatever other module you choose to install. Don't
forget to add it to the `modules_enabled` section in the config.

### Adding users

`prosodyctl` makes this a fairly simple task:

```
$ prosodyctl adduser user@chat.example.com
```

You will be prompted for a password. You can optionally, enable
user registrations from XMPP/Jabber clients (security risk!), by setting
`allow_registration = true`.

I may have missed something important, so here's [my
config](https://cdn.icyphox.sh/prosody.cfg.lua) for reference.

## Closing notes

That's pretty much all you need for 1-on-1 E2EE chats. I don't know much
about group chats just yet -- trying to create a group in Conversations
gives a "No group chat server found". I will figure it out later.

Another thing that doesn't work in Conversations is adding an account
using an `SRV` record.[^srv] Which kinda sucks, because having a `chat.`
subdomain isn't very clean, but whatever.

Oh, also -- you can message me at
[icy@chat.icyphox.sh](xmpp:icy@chat.icyphox.sh).

[^srv]: https://prosody.im/doc/dns
