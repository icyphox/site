---
template: text.html
title: Setting up my personal mailserver
subtitle: This is probably a terrible idea…
date: 2019-08-15
slug: mailserver
---

A mailserver was a long time coming. I'd made an attempt at setting one up
around ~4 years ago (ish), and IIRC, I quit when it came to DNS. And
I almost did this time too.[^1]

For this attempt, I wanted a simpler approach. I recall how terribly
confusing Dovecot & Postfix were to configure and hence I decided to look
for a containerized solution, that most importantly, runs on my cheap $5 
Digital Ocean VPS  --  1 vCPU and 1 GB memory. Of which only around 500 MB
is actually available. So yeah, *pretty* tight.

## What's available

Turns out, there are quite a few of these OOTB, ready to deply solutions.
These are the ones I came across:

- [poste.io](https://poste.io): Based on an "open core" model. The base install is open source 
and free (as in beer), but you'll have to pay for the extra stuff.

- [mailu.io](https://mailu.io): Free software. Draws inspiration from poste.io, 
but ships with a web UI that I didn't need. 

- [mailcow.email](https://mailcow.email): These fancy domains are getting ridiculous. But more importantly
they need 2 GiB of RAM *plus* swap?! Nope.

- [Mail-in-a-Box](https://mailinabox.email): Unlike the ones above, not a Docker-based solution but definitely worth
a mention. It however, needs a fresh box to work with. A box with absolutely 
nothing else on it. I can't afford to do that.

- [docker-mailserver](https://github.com/tomav/docker-mailserver/): **The winner**. 

## So… `docker-mailserver`

The first thing that caught my eye in the README:

> Recommended:
> 
> - 1 CPU
> - 1GB RAM
> 
> Minimum:
> 
> - 1 CPU
> - 512MB RAM

Fantastic, I can somehow squeeze this into my existing VPS.
Setup was fairly simple & the docs are pretty good. It employs a single
`.env` file for configuration, which is great.
However, I did run into a couple of hiccups here and there.

One especially nasty one was `docker` / `docker-compose` running out
of memory.
```
Error response from daemon: cannot stop container: 2377e5c0b456: Cannot kill container 2377e5c0b456226ecaa66a5ac18071fc5885b8a9912feeefb07593638b9a40d1: OCI runtime state failed: runc did not terminate sucessfully: fatal error: runtime: out of memory
```
But it eventually worked after a couple of attempts.

The next thing I struggled with  --  DNS. Specifically, the with the step where
the DKIM keys are generated[^2]. The output under  
`config/opendkim/keys/domain.tld/mail.txt`  
isn't exactly CloudFlare friendly; they can't be directly copy-pasted into
a `TXT` record. 

This is what it looks like.
```
mail._domainkey	IN	TXT	( "v=DKIM1; h=sha256; k=rsa; "
	  "p=<key>"
	  "<more key>" )  ;  -- -- DKIM key mail for icyphox.sh
```
But while configuring the record, you set "Type" to `TXT`, "Name" to `mail._domainkey`,
and the "Value" to what's inside the parenthesis `(  )`, *removing* the quotes `""`. 
Also remove the part that appears to be a comment `;  -- -- ...`.

To simplify debugging DNS issues later, it's probably a good idea to
point to your mailserver using a subdomain like `mail.domain.tld` using an 
`A` record.
You'll then have to set an `MX` record with the "Name" as `@` (or whatever your DNS provider
uses to denote the root domain) and the "Value" to `mail.domain.tld`.
And finally, the `PTR` (pointer record, I think), which is the reverse of 
your `A` record  --  "Name" as the server IP and "Value" as `mail.domain.tld`.
I learnt this part the hard way, when my outgoing email kept getting
rejected by Tutanota's servers.

Yet another hurdle  --  SSL/TLS certificates. This isn't very properly
documented, unless you read through the [wiki](https://github.com/tomav/docker-mailserver/wiki/Installation-Examples)
and look at an example. In short, install `certbot`, have port 80 free,
and run 

``` shell
$ certbot certonly --standalone -d mail.domain.tld
```

Once that's done, edit the `docker-compose.yml` file to mount `/etc/letsencrypt` in 
the container, something like so:
```yaml
...

volumes:
    - maildata:/var/mail
    - mailstate:/var/mail-state
    - ./config/:/tmp/docker-mailserver/
    - /etc/letsencrypt:/etc/letsencrypt

...
```

With this done, you shouldn't have mail clients complaining about 
wonky certs for which you'll have to add an exception manually.

## Why would you…?
There are a few good reasons for this:

### Privacy 
No really, this is *the* best choice for truly private
email. Not ProtonMail, not Tutanota. Sure, they claim so and I don't 
dispute it. Quoting Drew Devault[^3],

> Truly secure systems do not require you to trust the service provider.

But you have to *trust* ProtonMail. They run open source software, but
how can you really be sure that it isn't a backdoored version of it?

When you host your own mailserver, you truly own your email without having to rely on any
third-party.
This isn't an attempt to spread FUD. In the end, it all depends on your
threat model™.

### Decentralization
Email today is basically run by Google. Gmail has over 1.2 *billion*
active users. That's obscene.
Email was designed to be decentralized but big corps swooped in and
made it a product. They now control your data, and it isn't unknown that
Google reads your mail. This again loops back to my previous point, privacy.
Decentralization guarantees privacy. When you control your mail, you subsequently
control who reads it.

### Personalization
Can't ignore this one. It's cool to have a custom email address to flex.

`x@icyphox.sh` vs `gabe.newell4321@gmail.com`

Pfft, this is no competition.

[^1]: My [tweet](https://twitter.com/icyphox/status/1161648321548566528) of frustration.
[^2]: [Link](https://github.com/tomav/docker-mailserver#generate-dkim-keys) to step in the docs.
[^3]: From his [article](https://drewdevault.com/2018/08/08/Signal.html) on why he doesn't trust Signal.
