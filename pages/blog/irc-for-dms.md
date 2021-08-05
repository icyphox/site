---
template:
title: IRC for DMs
subtitle: Honestly, it's pretty great
date: 2019-11-03
slug: irc-for-dms
---

[Nerdy](https://nerdypepper.me) and I decided to try and use IRC for our
daily communications, as opposed to non-free alternatives like WhatsApp
or Telegram. This is an account of how that went.

## The status quo of instant messaging apps

I've tried a _ton_ of messaging applications -- Signal, WhatsApp,
Telegram, Wire, Jami (Ring), Matrix, Slack, Discord and more recently, DeltaChat.

**Signal**: It straight up sucks on Android. Not to mention the
centralized architecture, and OWS's refusal to federate.

**WhatsApp**: Facebook's spyware that people use without a second
thought. The sole reason I have it installed is for University's
class groups; I can't wait to graduate.

**Telegram**: Centralized architecture and a closed-source server. It's
got a very nice Android client, though.

**Jami**: Distributed platform, free software. I am not going to comment
on this because I don't recall what my experience was like, but I'm not
using it now... so if that's indicative of anything.

**Matrix (Riot)**: Distributed network. Multiple client implementations.
Overall, pretty great, but it's slow. I've had messages not send / not
received a lot of times. Matrix + Riot excels in group communication, but
really sucks for one-to-one chats.

**Slack** / **Discord**: _sigh_

**DeltaChat**: Pretty interesting idea -- on paper. Using existing email
infrastructure for IM sounds great, but it isn't all that cash in
practice. Email isn't instant, there's always a delay of give or take
5 to 10 seconds, if not more. This affects the flow of conversation.
I might write a small blog post later, revewing DeltaChat.[^deltachat]

## Why IRC?

It's free, in all senses of the word. A lot of others have done a great
job of answering this question in further detail, this is by far my
favourite:

https://drewdevault.com/2019/07/01/Absence-of-features-in-IRC.html

## Using IRC's private messages
 
This was the next obvious choice, but personal message buffers don't
persist in ZNC and it's very annoying to have to do a `/query
nerdypepper` (Weechat) or to search and message a user via Revolution
IRC. The only unexplored option -- using a channel.

## Setting up a channel for DMs

A fairly easy process:

* Set modes (on Rizon)[^modes]:

    ```
    #crimson [+ilnpstz 3]
    ```
    In essence, this limits the users to 3 (one bot), sets the channel to invite only,
hides the channel from `/whois` and `/list`, and a few other misc.
modes.

* Notifications: Also a trivial task; a quick modification to [lnotify.py](https://weechat.org/scripts/source/lnotify.py.html/)
to send a notification for all messages in the specified buffer
(`#crimson`) did the trick for Weechat. Revolution IRC, on the other
hand, has an option to setup rules for notifications -- super
convenient.

* A bot: Lastly, a bot for a few small tasks -- fetching URL titles, responding
to `.np` (now playing) etc. Writing an IRC bot is dead simple, and it
took me about an hour or two to get most of the basic functionality in
place. The source is [here](https://github.com/icyphox/detotated).
It is by no means "good code"; it breaks spectacularly from time to
time.

## In conclusion

As the subtitle suggests, using IRC has been great. It's probably not
for everyone though, but it fits my (and Nerdy's) usecase perfectly.

P.S.: _I'm not sure why the footnotes are reversed._

[^modes]: Channel modes on [Rizon](https://wiki.rizon.net/index.php?title=Channel_Modes).
[^deltachat]: It's in [queue](https://github.com/icyphox/site/issues/10).
