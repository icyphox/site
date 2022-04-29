---
template:
slug: building-forlater
title: How I built forlater.email
subtitle: A technical breakdown of my first big side-project
date: 2021-09-25
---

Ever since I began browsing sites like Hacker News and Lobsters, coming
across new and exciting links to check out every day, I found it hard to
keep up. On most days, I just didn't. And that's fine -- [good,
even](/blog/dont-news). But oftentimes, I'd come across a genuinely
interesting link but no time to actually read it.

I began using Pocket. It was alright -- the article view was very good;
but it stopped there. I didn't like nor use the other junk baked into
the app: discover, following/friends thing, etc. It's also proprietary,
and that irked me -- more so than the other "features".

Thus, somewhat inspired by rss2email, I began building
[forlater.email](https://forlater.email) -- a bookmarking/read-later
service that works via email. Email is the perfect tool for this
use-case: works offline; you can organize it however you like; you own
your data.

![forlater arch](https://cdn.icyphox.sh/JNAn4.png)

Pictured above is how forlater works. Each component is explained below.

## OpenSMTPD

Mail containing links to be saved arrive here. OpenSMTPD is beautiful
software, and its configuration is stupid simple
([smtpd.conf(5)](https://man.openbsd.org/smtpd.conf)):

```conf
table blocklist file:/etc/smtpd/blocklist

action webhook mda "/home/icy/forlater/mdawh/mdawh"
match mail-from <blocklist> for any reject
match from any for rcpt-to "save@forlater.email" action webhook
```

The `filter` and `listen` directives have been snipped for brevity. The
rest, in essence, simply sends all mail to `save@forlater.email` to an
MDA program, via stdin. Any mail from an address in the blocklist file
get rejected.

[rspamd](https://rspamd.com) is used to prevent spam.

## mdawh

[mdawh](https://git.icyphox.sh/forlater/mdawh), or the MDA webhook tool.
A small Go program that processes mail coming from stdin and generates a
JSON payload that looks like so:

```json
{
  "from": "foo@bar.com",
  "date": "Fri, 1 Jan 2010 00:00:00 UTC",
  "replyto": "...",
  "body": "...",
  "parts": {
    "text/plain": "...",
    "text/html": "...",
  }
}
```

This is POSTed to a configured HTTP endpoint -- which in this case, is
navani.

## navani

[navani](https://git.icyphox.sh/forlater/navani) is forlater's primary
mail processing service[^1]. Listens for webhooks from mdawh, processes
them, and sends mail using a configured SMTP server. URLs are cached in
Redis along with the HTML content.

For the readable HTML,
[go-readability](https://github.com/go-shiori/go-readability) is used;
the output of which is rendered into a minimal [HTML email
template](https://git.icyphox.sh/forlater/navani/tree/templates/html.tpl)
-- something that I never want to write again.

The plaintext part is currently generated using `lynx -image_links -dump
-stdin`. The `-image_links` flag is handy because it generates footnote
links for images as well, instead of simply ignoring images altogether.
I plan to rewrite this; possibly using a blend of HTML-to-plaintext
libraries and handwritten rules.

## future improvements

I plan to implement some kind of `settings@` address to configure and
store user settings (dark theme? fonts?). However, this introduces state
in an otherwise mostly stateless system.

The other thing I've been thinking of is making your own newsletter of
sorts. For example: save a bunch of links during the week, and have them
all delivered over the weekend.

Neither of these "features" are confirmed to happen, primarily because
forlater is feature-complete for my use. That said, I'm happy to
consider any improvements or suggestions that you might have -- please
[email me](mailto:x@icyphox.sh).

Finally, thanks to everyone who tossed a few bucks my way -- mighty kind
of you.

[^1]: Named after [Navani Kholin](https://coppermind.net/wiki/Navani_Kholin).
