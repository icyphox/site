---
template:
slug: mastodon-to-pleroma
title: Migrating from Mastodon to Pleroma
subtitle: Mastodon bad. Pleroma good.
date: 2020-09-04
---

If you've been following me on the fediverse, you would've witnessed my
numerous (failed) attempts at migrating from Mastodon to Pleroma,
running on my Raspberry Pi. I finally got it working, and these are the
steps I took. It's sort of a loose guide you could follow, but I can't
promise it'll work for you.

The Erlang and Elixir packages are pretty broken and outdated on
Raspbian. So this time, I built them from source.[^1][^2] I also assume
you have Mastodon and Pleroma (source, not OTP) installed -- probably at
`/home/mastodon/live` and `/opt/pleroma`, respectively.

Once you have Erlang and Elixir compiled and sitting in your `PATH`,
pull [soapbox-pub/migrator](https://gitlab.com/soapbox-pub/migrator).
Now read the readme and the `do_migration.sh` script to get an idea of
what you're getting into.

Move into the cloned directory and create a `.env`:

```shell
MASTODON_PATH=/home/mastodon/live
PLEROMA_PATH=/opt/pleroma
```

Then, run:

```console
$ yarn   # install deps
$ cp -r mastodon/* /home/mastodon/live
$ cp -r pleroma/* /opt/pleroma
$ RAILS_ENV=production yarn masto export
```

If you run into any permissions issues, `chown` and proceed. This should
export all your Mastodon activity into `/home/mastodon/live/migrator`.
Now, copy the `migrator` directory into your Pleroma installation path.

```console
$ cp -r migrator /opt/pleroma
```

You can then import all of it into Pleroma (possibly prefixed with `sudo
-Hu pleroma`):
```console
$ MIX_ENV=prod mix migrator.import
```

If all went well, you would've successfully migrated from Mastodon to
Pleroma. If not, well feel free to send me an email (or @ me on the fedi).
I suppose you could also reach [Alex](https://alexgleason.me) -- he's
the incredibly based guy who wrote the migrator,
[soapbox-fe](https://soapbox.pub) and does some Elixir magic he keeps
[posting about](https://gleasonator.com/@alex).

Rest assured, the migrator has a 100% success rate -- Alex and I are
apparently the only two who have it working. 2/2.

## why should you migrate?

Because Pleroma is cleaner, leaner[^3] and prettier looking[^4]. Oh, and we
have chats.
![screenshot of pleroma + soapbox-fe](https://cdn.icyphox.sh/l8g5y.png)

[^1]: [Erlang install guide](http://erlang.org/doc/installation_guide/INSTALL.html)
[^2]: [Elixir install guide](https://elixir-lang.org/install.html#compiling-from-source-unix-and-mingw)
[^3]: Mastodon used about ~2.5 GB out of the 4 I have on my Pi. With
      Pleroma, the total used RAM is only about ~700 MB. That's crazy!
[^4]: ...with Soapbox. :^)

