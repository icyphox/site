---
template:
slug: push
title: Push-based productivity
subtitle: Getting told when to get things done
date: 2025-01-03
---

Way back in 2021, I wrote about [my productivity endeavours][prod],
which were -- in summary -- me writing a list of todos in a notebook.
I still carry these around to quickly note stuff down or to summarise my
pursuits of the week every Sunday evening.

[prod]: /blog/bujo/
![notebooks](https://cdn.icyphox.sh/fit?url=http://files.garage.koti.lan/IMG_2558.jpg&width=1000&height=2000)

However, I quickly realised a glaring issue with this system: it needed
*me* to constantly check the notebook to learn of things to be done. For
me, this failed constantly:

* I didn't check it often enough and missed time-critical tasks
* I checked it but I *forgot* to do the thing because I was distracted

As an example, every so often during the day, I'd note down a task to
say "buy oat milk". Easy enough. I can do that on my way home from
work. There's a supermarket at my nearest metro station so popping by
there before walking home should be a trivial task.

Hardly so. I either never checked my todo list on the metro ride home,
or embarrassingly, I'd check and then proceed to immediately forget. The
sheer annoyance when I'd realize my lapse upon getting home and taking
out my notebook...

This is a problem inherent to any "pull-based" system -- one where the
user/client/whatever must "pull" (or poll!) for information at
intervals. Especially given that said information has an arbitrary TTL
in my head, and the poll interval is not fixed, there are several of
these blind spots where tasks get missed.

And so, my new push-based system -- one that I've been using to great
effect for the better part of last year -- came about. At its core it's
incredibly simple: my phone's Reminders app. I use Apple Reminders but
really, this works with any similar app.

Nothing revolutionary, I know. I'm just rather proud of how easy it was
to get setup and see positive results. I have mine setup against my
[self-hosted][sh] Radicale server. Separate lists to organize tasks and
a homescreen widget to quickly check off completed ones.

[sh]: /uses#homelab-k3s-cluster

<div class="row">
<img src="https://cdn.icyphox.sh/reminders.jpg" style="width: 240px;" alt="reminders">
<img src="https://cdn.icyphox.sh/hss.jpg" style="width: 240px;" alt="home screen widget">
</div>

For quick input, I've been in love with [Remind Me
Faster](https://apps.apple.com/us/app/remind-me-faster/id985555908). I'm
now able to rapidly create tasks, assign it a time[^1] and optionally, a
location. The latter, I find, is the killer feature. Being reminded of a
task *when* you're arriving/leaving (RMF lets you choose this) a
location is very powerful.

[^1]: Apple Calendar in iOS 18 onward now shows your reminders alongside
    other events. Very handy for scheduling.

<div class="row">
    <img src="https://cdn.icyphox.sh/IMG_2561.PNG" style="width: 240px;" alt="remind me faster">
    <img src="https://cdn.icyphox.sh/IMG_2563.jpg" style="width: 240px;" alt="setting time and location">
</div>

I now get reminded to "buy oat milk" when I'm arriving at the metro
station's shopping center.[^2] And to post this once I get home.

[^2]: _kauppakeskus_ in Finnish.
