---
template:
slug: honk-fly
title: Honkin' on the Fly
subtitle: Running honk on fly.io
date: 2022-05-25
---

**Update 2022-08-11**: As with literally every update of mine, I'm no
longer running honk on Fly. It's way easier to simply run it on a server
myself, behind nginx. Huh -- who knew?

For those unaware -- first of all, how? it's literally everywhere --
[fly.io](https://fly.io) is the new platform-as-a-service du jour. The
idea is to give them a Dockerfile (or a pre-built image, or just generic
applications in [a bunch of
languages](https://fly.io/docs/getting-started/#language-guides)), and
they run it for you on servers across the globe. Firecracker microVMs,
WireGuard, and some other neat tech. Understandably, this gets the
average Hacker News-type (me), excited. And I'd been meaning to switch
my fediverse instance over to
[honk](https://humungus.tedunangst.com/r/honk) -- a stateful Go
application using sqlite[^1]. And the fly.io folks [really like
sqlite](https://fly.io/blog/all-in-on-sqlite-litestream/). The stars
have aligned.

[^1]: Written by [tedu](https://honk.tedunangst.com/u/tedu). He's a cool
      guy who runs and hacks OpenBSD. The honk source is a fun read.

I trust that you can figure out the initial setup bits like logging in
to the dashboard and giving them your credit card info and praying that
they don't run you a bill of $5000 because you somehow blew through
their free allowance resources. As I understand it, Fly "auto-scales",
so this scenario isn't unlikely -- however, [they do offer some
leniency](https://news.ycombinator.com/item?id=31392497). Luckily, the
chances of me turning into a fedi-influencer (_fedifluencer_?) overnight
are rather slim.

## setup

They want a Dockerfile, so let's give them one.

```dockerfile
FROM golang:1.18-alpine AS builder
RUN apk add sqlite-dev build-base mercurial

WORKDIR /tmp/src
RUN hg clone https://humungus.tedunangst.com/r/honk 
RUN cd honk && make

FROM alpine:latest
RUN apk add sqlite sqlite-dev

COPY local /tmp/local
COPY memes /tmp/memes
COPY emus /tmp/emus

WORKDIR /opt
COPY --from=builder /tmp/src/honk/honk /bin/
COPY --from=builder /tmp/src/honk/views views/
COPY start /bin

ENV HONK_DATA_DIR "/opt/data"
ENV HONK_VIEWS_DIR "/opt/"

CMD ["/bin/start"]
```

Not too much going on here -- we pull latest tip, build honk, copy the
`local` directory containing our `local.css` (custom styles); the
`memes` directory containing, well, memes (PNGs and GIFs); and the
`emus` directory containing emoji (used as `:filename:`). These will
then be copied into the Fly volume later on by the `start` script. Kinda
gross, but whatever.

And the `start` script:

```sh
#!/bin/sh

run() {
    cp -R /tmp/memes/* "$HONK_DATA_DIR"/memes/
    cp -R /tmp/memes/* "$HONK_DATA_DIR"/emus/
    cp -R /tmp/local/* "$HONK_DATA_DIR"/views/

    honk -datadir "$HONK_DATA_DIR" -viewdir "$HONK_VIEWS_DIR"
}

# first time setup
if [ ! -f "$HONK_DATA_DIR/honk.db" ]; then
    honk init <<-EOF
    $HONK_USERNAME
    $HONK_PASSWORD
    $HONK_ADDRESS
    $HONK_SERVER_NAME
    EOF
fi

run
```

This simply copies our stuff from the container into the volume, and
launches honk. If the honk database doesn't yet exist, we run `honk
init` and set it up. These environment variables are configured in the
`fly.toml` file:

```toml
app = "honk"

kill_signal = "SIGINT"
kill_timeout = 5
processes = []

[mounts]
  source = "honkstore"
  destination = "/opt/data"

[env]
  HONK_USERNAME = "icy"
  HONK_ADDRESS = "0.0.0.0:8080"
  HONK_SERVER_NAME = "h.icyphox.sh"

[experimental]
  allowed_public_ports = []
  auto_rollback = true

[[services]]
  http_checks = []
  internal_port = 8080
  processes = ["app"]
  protocol = "tcp"
  script_checks = []

  [services.concurrency]
    hard_limit = 50
    soft_limit = 20
    type = "connections"

  [[services.ports]]
    force_https = true
    handlers = ["http"]
    port = 80

  [[services.ports]]
    handlers = ["tls", "http"]
    port = 443

  [[services.tcp_checks]]
    grace_period = "1s"
    interval = "15s"
    restart_limit = 0
    timeout = "2s"
```

The `fly.toml` gets generated when you first run `fly launch`. The only
bits I've added are the `env` and `mounts` sections. Notice that
`HONK_PASSWORD` is missing, and for good reason -- Fly has support for
secrets, which can be created quite handily using:

```sh
$ flyctl secrets set HONK_PASSWORD="$(pw -s honk)"
```

## deploy

The only thing left to do is to provision our volume for persistence,
and we're off to the races:

```sh
$ flyctl volumes create honkstore --region maa
        ID: vol_1g67340omkm4ydxw
      Name: honkstore
       App: honk
    Region: maa
      Zone: aed0
   Size GB: 10
 Encrypted: true
Created at: 21 May 22 16:07 UTC

$ flyctl deploy
```

## post-deploy

I like having pretty usernames. In this case, I want to drop the `h.`
subdomain and have it look like this: `icy@icyphox.sh`. To do this, we
simply set the `masqname` key in the database to our desired
hostname[^2]:

```sh
$ honk setconfig 'masqname' 'icyphox.sh'
```

[^2]: Had to setup a custom domain for this: https://fly.io/docs/app-guides/custom-domains-with-fly/

And at `icyphox.sh`, we setup a redirect to `h.icyphox.sh` at the
`/.well-known/webfinger` path. I did this [via
Netlify](https://github.com/icyphox/site/commit/4bbc8335481a0466d7c23953b0f6057f97607ed1);
you can do it however, as long as the query parameters are preserved.
Read more about webfingers and other thingamabobs
[here](https://docs.joinmastodon.org/spec/webfinger/).

I did a bunch more like custom CSS, avatars etc. but I'll leave that as
homework for you
([honk(8)](https://humungus.tedunangst.com/r/honk/m/honk.8) is mandatory
reading!).

## thoughts

**On Fly**: I think it's neat. Rough edges? Sure. My [deploy was stuck
in
`pending`](https://community.fly.io/t/app-stuck-in-pending-in-maa-region/5280);
I had to delete it and re-create it for it to start working again. I
lost my data in the process because volumes are attached to apps.
Perhaps I should've waited and the problem would've fixed itself. Who
knows? 

And that's the eternal problem with PaaS -- there's a layer of
abstraction that you can't ever pierce. You can't truly know what the
problem was unless they publish a post-mortem (or don't). Anyway, in
this case I'll just chalk it up to teething issues.

Is it easier than simply building it on a server and running `nohup
./honk &` and calling it a day[^3]? Not really. It's more fun, I guess.

[^3]: Yes that's actually how I run a bunch of my services, including
      [forlater.email](https://forlater.email)!

**On honk**: It's refreshing. I liked running Pleroma + Soapbox (I still
do, haven't killed it yet), but it always felt alien to me. I didn't
understand the code, didn't enjoy having to upgrade Elixir/Erlang OTP
whatever, `mix.deps get` blah blah; a single Go binary + sqlite + HTML
templates speaks to me.

Go follow me at [icy@icyphox.sh](https://h.icyphox.sh/u/icy). It's why I
even wrote this post. Not that I can see it, honk doesn't have those
ego-numbers.

You can find all the source code to deploy honk yourself here:
https://git.icyphox.sh/honk
