---
template:
slug: signal
title: We can do better than Signal
subtitle: Centralized silos are never the solution
date: 2021-01-17
---

Signal is possibly the most recommended pro-privacy instant
communication app -- one that was commonplace in the hacker community,
and has now gained a lot of mainstream traction, thanks to WhatsApp
deciding to screw its userbase over. It certainly presents a more
compelling alternative than others in the same space, like WhatsApp
itself, Telegram, etc. They engineered the [Signal
Protocol](https://en.wikipedia.org/wiki/Signal_Protocol), which has
found its way into other messaging systems, and has been the base for
the likes of OMEMO and Matrix.[^1] While I admire the tech behind
Signal, I still believe we can do better, and we ought to.

[^1]: https://en.wikipedia.org/wiki/Double_Ratchet_Algorithm

I have a few gripes with Signal -- the biggest of them all is it's
centralized, and in the US no less. This alone makes it not that
different from WhatsApp -- we're simply moving from one silo to another.
What's to say that Signal will uphold its values, continue operating
_and_ evade censorship and potential compromise? To top it off, they're
becoming a fairly high value target off late. And if that isn't
convincing enough, Signal's massive outage lasting nearly a day[^2]
should be enough evidence against centralization. Further, Signal is
known to use AWS[^3] as their cloud provider -- what if another
Parler[^4] happens and the rug is pulled from under Signal's feet?

[^2]: https://twitter.com/signalapp/status/1350595202872823809
[^3]: https://signal.org/blog/looking-back-on-the-front/
[^4]: https://en.wikipedia.org/wiki/Parler#Shutdown_by_service_providers

A common defense in favor of Signal is, "But it's all open source!".
Sure is, but on what basis do I trust them? I don't mean to sound
conspiratorial, but what's to say that the server in production hasn't
been backdoored? In fact, the [Signal server
code](https://github.com/signalapp/Signal-Server) hasn't even been
updated since April 2020. You're telling me it's undergone _no_ changes?

Another response I usually see is "But Signal is all we have!". While
that is somewhat true -- at least by the metric of "secure messengers
your granny can use", there are some promising alternatives who are
especially focused on decentralizing E2EE communications.

1. [Matrix](https://matrix.org): Matrix has improved a whole lot, and I
   like that they're working to disprove that end-to-end encryption
   cannot be decentralized[^5].
2. [Session](https://getsession.org): While it involves some cryptoshit,
   and hasn't been verified yet, it's an interesting alternative to keep
   an eye out for.

[^5]: https://matrix.org/blog/2020/01/02/on-privacy-versus-freedom

All things said, Signal is the shiniest turd we have -- it fits most
threat models, and does the job alright; I will continue to use it.
However, here's something to think about: while privacy preserving tech
is commendable, does it have to come at the cost of user freedoms? Hint:
it doesn't, and it shouldn't.
