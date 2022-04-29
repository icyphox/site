---
template:
title: Instagram OPSEC
subtitle: Operational security for the average zoomer
date: 2019-12-02
slug: ig-opsec
---

Which I am not, of course. But seeing as most of my peers are, I am
compelled to write this post. Using a social platform like Instagram
automatically implies that the user understands (to some level) that
their personally identifiable information is exposed publicly, and they
sign up for the service understanding this risk -- or I think they do,
anyway. But that's about it, they go ham after that. Sharing every nitty
gritty detail of their private lives without understanding the potential
risks of doing so.

The fundamentals of OPSEC dictacte that you develop a threat model, and
Instgrammers are _obviously_ incapable of doing that -- so I'll do it
for them. 

## Your average Instagrammer's threat model

I stress on the word "average", as in this doesn't apply to those with
more than a couple thousand followers. Those type of accounts inherently
face different kinds of threats -- those that come with having
a celebrity status, and are not in scope of this analysis.

- **State actors**: This doesn't _really_ fit into our threat model,
since our target demographic is simply not important enough. That said,
there are select groups of individuals that operate on
Instagram[^ddepisode], and they can potentially be targetted by a state
actor.

[^ddepisode]: https://darknetdiaries.com/episode/51/ -- Jack talks about Indian hackers who operate on Instagram.

- **OSINT**: This is probably the biggest threat vector, simply because
of the amount of visual information shared on the platform. A lot can be
gleaned from one simple picture in a nondescript alleyway. We'll get
into this in the DOs and DON'Ts in a bit.

- **Facebook & LE**: Instagram is the last place you want to be doing an
illegal, because well, it's logged and more importantly -- not
end-to-end encrypted. Law enforcement can subpoena any and all account
information. Quoting Instagram's 
[page on this](https://help.instagram.com/494561080557017):

>a search warrant issued under the procedures described in the Federal 
>Rules of Criminal Procedure or equivalent state warrant procedures 
>upon a showing of probable cause is required to compel the disclosure 
>of the stored contents of any account, which may include messages, 
>photos, comments, and location information.

That out of the way, here's a list of DOs and DON'Ts to keep in mind
while posting on Instagram.

### DON'Ts

- Use Instagram for planning and orchestrating illegal shit! I've
explained why this is a terrible idea above. Use secure comms -- even
WhatsApp is a better choice, if you have nothing else. In fact, try
avoiding IG DMs altogether, use alternatives that implement E2EE.

- Film live videos outside. Or try not to, if you can. You might
unknowingly include information about your location: street signs,
shops etc. These can be used to ascertain your current location.

- Film live videos in places you visit often. This compromises your
security at places you're bound to be at.

- Share your flight ticket in your story! I can't stress this enough!!!
Summer/winter break? "Look guys, I'm going home! Here's where I live,
and here's my flight number -- feel free to track me!". This scenario is
especially worrisome because the start and end points are known to the
threat actor, and your arrival time can be trivially looked up -- thanks
to the flight number on your ticket. So, just don't.

- Post screenshots with OS specific details. This might border on
pendantic, but better safe than sorry. Your phone's statusbar and navbar 
are better cropped out of pictures. They reveal the time, notifications
(apps that you use), and can be used to identify your phone's operating
system.  Besides, the status/nav bar isn't very useful to your screenshot 
anyway.

- Share your voice. In general, reduce your footprint on the platform
that can be used to identify you elsewhere.

- Think you're safe if your account is set to private. It doesn't take
much to get someone who follows you, to show show your profile on their
device.

### DOs

- Post pictures that pertain to a specific location, once you've moved
out of the location. Also applies to stories. It can wait.

- Post pictures that have been shot indoors. Or try to; reasons above.
Who woulda thunk I'd advocate bathroom selfies?

- Delete old posts that are irrelevant to your current audience. Your
friends at work don't need to know about where you went to high school.

More DON'Ts than DOs, that's very telling. Here are a few more points
that are good OPSEC practices in general:

- **Think before you share**. Does it conform to the rules mentioned above?
- **Compartmentalize**. Separate as much as you can from what you share
online, from what you do IRL. Limit information exposure.
- **Assess your risks**: Do this often. People change, your environments
change, and consequentially the risks do too.

## Fin

Instagram is -- much to my dismay -- far too popular for it to die any
time soon. There are plenty of good reasons to stop using the platform
altogether (hint: Facebook), but that's a discussion for another day.

Or be like me:

![](https://cdn.icyphox.sh/fI7nL.jpg)


And that pretty much wraps it up, with a neat little bow.

