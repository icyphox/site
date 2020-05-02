---
template:
url: s-nail
title: The S-nail mail client
subtitle: And how to achieve a usable configuration for IMAP/SMTP
date: 2020-04-30
---

TL;DR: Here's my [`.mailrc`](https://github.com/icyphox/dotfiles/blob/master/home/.mailrc).

As I'd mentioned in my blog post about [mael](/blog/mael), I've been on
the lookout for a good, usable mail client. As it happens, I found
S-nail just as I was about to give up on mael. Turns out writing an MUA
isn't all too easy after all. S-nail turned out to be the perfect client
for me, but I had to invest quite some time in reading the [very
thorough manual](https://www.sdaoden.eu/code-nail.html) and exchanging
emails with its [very friendly author](https://www.sdaoden.eu). I did it
so you don't have to[^read-man], and I present to you
this guide.

[^read-man]: Honestly, read the man page (and email Steffen!)---there's
    a ton of useful options in there.

## basic settings

These settings below should guarantee some sane defaults to get started
with. Comments added for context.
```conf
# enable upward compatibility with S-nail v15.0
set v15-compat

# charsets we send mail in
set sendcharsets=utf-8,iso-8859-1

# reply back in sender's charset
set reply-in-same-charset

# prevent stripping of full names in replies
set fullnames

# adds a 'Mail-Followup-To' header; useful in mailing lists
set followup-to followup-to-honour-ask-yes

# asks for an attachment after composing
set askattach

# marks a replied message as answered
set markanswered

# honors the 'Reply-To' header
set reply-to-honour

# automatically launches the editor while composing mail interactively
set editalong

# I didn't fully understand this :) 
set history-gabby=all

# command history storage
set history-file=~/.s-nailhist

# sort mail by date (try 'thread' for threaded view)
set autosort=date
```

## authentication

With these out of the way, we can move on to configuring our
account---authenticating IMAP and SMTP. Before that, however, we'll
have to create a `~/.netrc` file to store our account credentials. 

(This of course, assumes that your SMTP and IMAP credentials are the
same. I don't know what to do otherwise. )

```netrc
machine *.domain.tld login user@domain.tld password hunter2
```

Once done, encrypt this file using `gpg` / `gpg2`. This is optional, but
recommended.

```
$ gpg2 --symmetric --cipher-algo AES256 -o .netrc.gpg .netrc
```

You can now delete the plaintext `.netrc` file. Now add these lines to
your `.mailrc`:

```conf
set netrc-lookup
set netrc-pipe='gpg2 -qd ~/.netrc.gpg'
```

Before we define our account block, add these two lines for a nicer IMAP
experience:

```conf
set imap-cache=~/.cache/nail
set imap-keepalive=240
```

Defining an account is dead simple. 

```conf
account "personal" {
    localopts yes
    set from="Your Name <user@domain.tld>"
    set folder=imaps://imap.domain.tld:993

    # copy sent messages to Sent; '+' indicates subdir of 'folder' 
    set record=+Sent
    set inbox=+INBOX
    
    # optionally, set this to 'smtps' and change the port accordingly
    # remove 'smtp-use-starttls'
    set mta=smtp://smtp.domain.tld:587 smtp-use-starttls

    # couple of shortcuts to useful folders
    shortcut sent +Sent \
        inbox +INBOX \
        drafts +Drafts \
        trash +Trash \
        archives +Archives
}

# enable account on startup
account personal
```
