---
template:
slug: simplicity-security
title: Simplicity (mostly) guarantees security
subtitle: This is why I meme mnmlsm so much
date: 2020-05-07
---

Although it is a very comfy one, it's not just an aesthetic. Simplicity
and minimalism, in technology, is great for security too. I say "mostly"
in the title because human error cannot be discounted, and nothing is
perfect. However, the simpler your tech stack is, it is inherentely more
secure than complex monstrosities.

Let's look at systemd, for example. It's got over 1.2 million
lines of code. "Hurr durr but LoC doesn't mean anything!" Sure ok, but
can you _imagine_ auditing this? How many times has it even been
audited? I couldn't find any audit reports. No, the developers are not
security engineers and a trustworthy audit must be done by
a third-party. What's scarier, is this thing runs on a huge percentage 
of the world's critical infrastructure and contains privileged core
subsystems. 

"B-but Linux is much bigger!" Indeed, it is, but it has a thousand times
(if not more) the number of eyes looking at the code, and there have been
multiple third-party audits. There are hundreds of independent orgs and
multiple security teams looking at it. That's not the case with
systemd -- it's probably just RedHat.

Compare this to a bunch of shell scripts. Agreed, writing safe shell can
be hard and there are a ton of weird edge-cases depending on your shell
implementation, but the distinction here is _you_ wrote it. Which means,
you can identify what went wrong -- things are predictable.
systemd, however, is a large blackbox, and its state at runtime is largely
unprovable and unpredictable. I am certain even the developers don't
know.

And this is why I whine about complexity so much. A complex,
unpredictable system is nothing more than a large attack surface. Drew
DeVault, head of [sourcehut](https://sourcehut.org) wrote something
similar (yes that's the link, yes it has a typo).: 

https://sourcehut.org/blog/2020-04-20-prioritizing-simplitity/

He manually provisions all
sourcehut infrastructure, because tools like Salt, Kubernetes etc. are
just like systemd in our example -- large monstrosities which can get you
RCE'd. Don't believe me? See 
[this](https://threatpost.com/salt-bugs-full-rce-root-cloud-servers/155383/).

*This was day 3 of the #100DaysToOffload challenge. It came out like
a systemd-hate post, but really, I couldn't think of a better example.*
