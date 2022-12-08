---
template:
slug: cloud-foss
title: Cloud (F)OSS is a good model
subtitle: On building (mostly) open source startups
date: 2022-02-07
---

Of late, I've been thinking a lot about what makes a startup work, and I
think open sourcing your product -- or a good portion of it -- is a
great approach. To be clear, I'm only talking about SaaS platforms, and
not any other kind of product. Hence, I'm dubbing this as "Cloud FOSS".

The title of this post was initially "Cloud FOSS is the way", but I
quickly realised that I know next to nothing about actually building
companies and I'm really just talking out of my rear end. Nevertheless
it's still pretty fun to try and reason about why the open source model
is great for startups, so reason we shall.

Broadly speaking, there are two kinds of "Cloud FOSS" companies:
- the open source and cloud versions are identical, entirely free software (à la
  [sourcehut](https://sourcehut.org))
- the cloud version has exclusive "premium" features that aren't present
  in the open source version -- a.k.a the open core model; it seems to
  be gaining a lot of popularity in recent times with the likes of
  Gitlab etc.

Let's dissect each approach and see what drives them.

## the all-FOSS absolutist model

As mentioned above, sourcehut is a great -- if not the only -- example
of a company built this way. Unless of course, I'm gravely mistaken
(wouldn't be the first time!), and you know of another, or are building
one yourself -- please [email me](mailto:x@icyphox.sh); I'll be happy to
mention it here.

**Update**: I was indeed mistaken. Here are a few companies built
similarly:
- [jmp.chat](https://jmp.chat/) -- free-as-in-freedom US/Canadian phone
  numbers
- [Frappe](https://frappe.io/) -- Indian company building a suite of
  free software products
- [Plausible Analytics](https://plausible.io) -- free software analytics
  platform. The self-hosted version has a less frequent (LTS) release
  schedule.

For those unaware, sourcehut is an entirely free software
company/startup that's building a software development platform; a suite
of tools and services like git/hg hosting, CI, mailing lists, issue
tracking etc. All of these can be self-hosted, with [plenty of
docs](https://man.sr.ht/installation.md) to get started doing so. Or,
you can of course, pay for the hosted service at [sr.ht](https://sr.ht),
their flagship instance.

Granted, this one's probably quite hard to pull off, especially if you're VC
backed or have investors of any kind. When your product is free
software, you can't really bake in analytics and other creepy
user-tracking shit that's common these days; what pages perform better,
what buttons do users click more often, the likes. And naturally, you
don't really have metrics to show your investors that your latest
feature du jour is doing great (or not).

Thankfully for us, sourcehut is completely bootstrapped. They've
[written
about](https://sourcehut.org/blog/2022-01-09-how-does-our-business-work/)
their business model, and it's beautifully simple: they make money from
users subscribing to their service -- the hosted version of the
sourcehut software -- and from other free software consultation gigs.
That's it. And they're quite profitable. Very cool sourcehut.

## the less absolutist open core model

The open core model, according to Wikipedia's definition:

> primarily involves offering a "core" or feature-limited version of a
> software product as free and open-source software, while offering
> "commercial" versions or add-ons as proprietary software.

Typically in SaaS offerings, the "commercial" version is a hosted
version of the open source software, _plus_ the usual suspects like
analytics, project management, user management, and a seat count for
different subscription tiers. Some startups may simply continue to
operate this way, with feature parity between the open source and cloud
versions (minus the meta "features"); however, this may not always be
the case.

Oftentimes, in accordance with the definition above, the open source
version may be _feature-limited_, with some parts of the core feature
set only available on the cloud version. In most cases, this probably
doesn't matter to the average self-hoster, since the paywalled features
will most likely be irrelevant to them -- usually catering to larger
deployments (support for say, CockroachDB), or enterprise-level
deployments (Active Directory support, SSO), etc.

The business model is quite straightforward -- get initial traction via
the self-hosted open source software, while building out your cloud
offering. The community built around the self-hosted software are your
initial pool of potential paying customers. Generally, these are either
early-stage startups (seed to series A) who don't have a large enough
team to manage additional infrastructure, or large enterprises who are
happy to pay for well, the enterprise features. These enterprise deals
may even transition into large on-prem contracts.

One thing to note about most open core projects is they'll most likely
enforce a CLA or a Contributor License Agreement. This usually says
something to the effect of "while you own the copyright to your code,
you grant us the rights to make money off it, or even relicense it
should we wish to do so". It's [probably not a good
idea](https://drewdevault.com/2018/10/05/Dont-sign-a-CLA.html) to sign
one.

## why cloud FOSS works

Cloud FOSS as a basis for building a company probably works because of a
bunch of reasons. As a startup, getting an initial foothold in the
market can be hard, and offering a fully open source version of your
platform can simplify that a whole lot. Setup a GitHub organization, do
a Show HN and Bob's your uncle. Obviously, it isn't _that_ easy, but you
get the idea.

Having an initial userbase from open source can be very useful. You
essentially get free insight into what features work and what don't,
and what features your users want. You also get bug reports, issues from
various deployment scenarios, environments, operating systems, etc. A
goldmine of information to help drive product development decisions.

Further, having a community built around your product helps too. High
quality contributors (sometimes), an audience for PR events, the ability
to conduct user surveys and most importantly, a hiring pool.

With that concludes my ideas on why Cloud FOSS is a good way to build a
startup. Again, I must reiterate that I literally have no idea what I'm
talking about and whatever I posit is merely a result of "Oh I've seen
it work this way before". I'm happy to hear what you think.

<hr>

This post was inspired by a conversation with
[Prithu](https://prithu.dev).
