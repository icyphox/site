---
template:
slug: mael
title: Introducing mael
subtitle: An experimental mail client
date: 2020-03-29
---

**Update**: The code lives here: https://github.com/icyphox/mael

I've been on the lookout for a good terminal-based email client since
forever, and I've tried almost all of them. The one I use right now
sucks a little less -- [aerc](https://git.sr.ht/~sircmpwn/aerc). I have
some gripes with it though, like the problem with outgoing emails not
getting copied to the Sent folder, and instead erroring out with
a cryptic `EOF` -- that's literally all it says.
I've tried mutt, but I find it a little excessive. It feels like the
weechat of email -- to many features that you'll probably never use.

I need something clean and simple, less bloated (for the lack of
a better term). This is what motivated me to try writing my own. The
result of this (and not to mention, being holed up at home with nothing
better to do), is **mael**.[^oss]

[^oss]: I have yet to open source it; this post will be updated with
    a link to it when I do.

mael isn't like your usual TUI clients. I envision this to turn out
similar to mailx -- a prompt-based UI. The reason behind this UX decision
is simple: it's easier for me to write. :)

Speaking of writing it, it's being written in a mix of Python and bash.
Why? Because Python's `email` and `mailbox` modules are fantastic, and
I don't think I want to parse Maildirs in bash. "But why not pure
Python?" Well, I'm going to be shelling out a lot (more on this in a bit), 
and writing interactive UIs in bash is a lot more intuitive, thanks to
some of the nifty features that later versions of bash have -- `read`,
`mapfile` etc.

The reason I'm shelling out is because two key components to this
client, that I haven't yet talked about -- `mbsync` and `msmtp` are in
use, for IMAP and SMTP respectively. And `mbsync` uses the Maildir
format, which is why I'm relying on Python's `mailbox` package. Why is
this in the standard library anyway?!

The architecture of the client is pretty interesting (and possibly very
stupid), but here's what happens:

- UI and prompt stuff in bash
- emails are read using `less`
- email templates (RFC 2822) are parsed and generated in Python
- this is sent to bash in STDOUT, like

```sh
msg="$(./mael-parser "$maildir_message_path")"
```

These kind of one-way (bash -> Python) calls are what drive the entire
process. I'm not sure what to think of it. Perhaps I might just give up
and write the entire thing in Python.
Or...I might just scrap this entirely and just shut up and use aerc.
I don't know yet. The code does seem to be growing in size rapidly. It's
about ~350 LOC in two days of writing (Python + bash). New problems
arise every now and then and it's pretty hard to keep track of all of
this. It'll be cool when it's all done though (I think).

If only things just worked.
