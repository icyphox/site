---
template:
slug: free-sw-censor
title: Free software should not censor
subtitle: If you write free software, don't deny freedom zero
date: 2021-04-07
---

Any software is free, if it grants the users the four essential
freedoms:

- **freedom 0**: The freedom to run the program as you wish, for any
  purpose.
- **freedom 1**: The freedom to study how the program works, and change
  it so it does your computing as you wish 
- **freedom 2**: The freedom to redistribute copies so you can help
  others.
- **freedom 3**: The freedom to distribute copies of your modified
  versions to others.

Denying any one of these freedoms makes your software nonfree. As it
happens, some free software project maintainers think it's OK to impose
their political / ideological stances on who can use their software, and
for what purpose it can be used. They are violating the zeroth freedom
to advance their political agendas. Here are a couple of examples.

## case one: Tusky

Tusky is a free software (GPL 3.0) Android client for the fediverse --
thematically, Mastodon. They [Rick Roll users who try to connect to
instances](https://github.com/tuskyapp/Tusky/pull/1303) they disagree
with. You don't get to decide for your users! And the irony here is its
a client for a supposedly censorship-resistant network. This is in
violation of freedom zero.

Funnily enough, Tusky recently got [removed from the Play
Store](https://chaos.social/@ConnyDuck/105904002285019275) for serving
"objectionable content".

> They don't seem to understand that one can view any content with Tusky
> and that it is not possible for the app developers to check any of it.
> -- https://chaos.social/@ConnyDuck/105904015276457450

A blatant lie! Doesn't feel good when someone else decides things for
you, now, does it?

## case two: Lemmy

Also a fediverse application -- a federated Reddit clone (AGPL 3.0).
They have a [hardcoded slur
filter](https://github.com/LemmyNet/lemmy/issues/622) that they refuse
to remove, or at the very least, make configurable. This is just plain
bad engineering for the sake of politics.

Both of these software are released under free software licenses, and
are clearly nonfree. Stop doing this -- it benefits nobody. You probably
feel like you're "making a change", but guess what: you're not. It is
mere virtue signalling. Don't enforce your political agendas on your
users.

Censorship is bad for everyone, and it usually never ends well.  There
is no "correct" way to censor -- so don't even try! If you don't want
your software to be "misused", release it under a license that is
capable of enforcing that.[^1]

[^1]: Protip: you can't. Ethical source licenses exist, but they're practically dead in the water.
