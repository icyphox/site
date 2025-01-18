---
template:
slug: identity
title: atproto and ownership of identity
subtitle: The new age of social-enabled apps
date: 2025-01-18
---

[atproto](https://atproto.com) is very exciting to me as it's the
perfect abstraction between the identity and user data layer, and the
application layer. Compare that to the fediverse and some striking
differences become apparent.

On the fediverse, your application -- Mastodon, Pleroma, WriteFreely,
whatever -- and your user account are tied together. Your presence on say
fosstodon.org isn't the same as what you'd use on Lemmy. This is
partially due to both services implementing entirely different schemas
of the ActivityPub spec[^1], and due to how AP addressing works: so
@user@fosstodon.org is fundamentally distinct from @user@lemmy.ml.

[^1]: Or in case of the Big M, doing things mostly their own way.

atproto solves this using Personal Data Servers (PDS)[^2] and
domain-based identities. This now allows for two levels of ownership:
1. **Ownership of identity**: Use your own domain and now that's your
   account across all of atproto.
2. **Ownership of data**: Run your own PDS and store all of your data
   yourself.

[^2]: [atproto for distributed systems
    engineers](https://atproto.com/articles/atproto-for-distsys-engineers) is recommended reading.

Thanks to this, users can re-use the same [DID](https://atproto.com/guides/identity)
across other apps built on atproto. Consequently, new social apps have
their two biggest problems solved for free:

1. The need for a new account (for users), and
2. The social graph.

This paves the way for all kinds of new "social-enabled" services to
emerge: forums, long-form writing, and potentially even more complex
ones like code forges and more -- all sharing the same account. The same
behavior is rather cumbersome in the above fediverse model because of
poor interoperability and lack of unified identity.

Further, the separation of the app and user layers now allows for
building "apps" that are viable businesses. The app layer can be a
monetized service much like Bluesky's supposed "premium" model that's in
the works. This is a good thing -- a financially viable open network is
one that sticks around longer.

There's also signs of early VC interest in atproto.
[skyseed.fund](https://skyseed.fund/) is a fund focused solely on
backing atproto projects. I predict this is the first of many. Given
that building on atproto is so much easier than building a traditional
social app from ground up, startups here can be small and scrappy
without needing much seed capital to take off. Bluesky already having
done the hard part of acquiring its 27M strong userbase, as of this
writing, is the icing on the cake.

So yes, bottom line, I think atproto has a promising future. There's a
ton of cool stuff being built atop it already and as the network and
protocol improve, I predict a new age of social apps with user-owned
identity at its core.
