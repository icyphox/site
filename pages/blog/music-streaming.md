---
template:
slug: music-streaming
title: My music streaming setup
subtitle: Think Spotify, but self-hosted and not as good
date: 2020-12-13
---

Having a self-hosted, centralized music streaming setup has been on my
todo list for the longest time. I'd initially tried using NFS, but
mounting it on my phone was very inconvenient. Incidentally, a few days
ago, the existence of Subsonic/*sonic became known to me.

## gonic

I found [gonic](https://github.com/sentriz/gonic) to be the simplest of
them all, and proceeded to set it up on the RPi. There are other
alternatives too, like [Navidrome](https://www.navidrome.org), which
ships with a web player, or [Airsonic](https://airsonic.github.io/).
gonic stood out the most to me because it's effectively headless,
barring a simple web interface for configuration.

Setting it up was trivial. I did run into an
[issue](https://github.com/sentriz/gonic/issues/89) -- I noticed that
only songs that were already in folders, sorted by album, were being
picked up in the scan.

```
|-- Void Of Vision - Hyperdaze (2019)
|   |-- 01. Overture.mp3
|   |-- 02. Year of the Rat.mp3
|   |-- 03. Babylon.mp3
|   |-- 04. If Only.mp3
|   |-- 05. Slave to the Name.mp3
|   |-- 06. Adrenaline.mp3
|   |-- 07. Hole In Me.mp3
|   |-- 08. Kerosene Dream.mp3
|   |-- 09. Decay.mp3
|   |-- 10. Splinter.mp3
|   |-- 11. Hyperdaze.mp3
|-- Volumes - Disaster Vehicle.mp3
|-- Volumes - Finite.mp3
|-- Volumes - Heavy Silence.mp3
|-- Volumes - Hope.mp3
|-- Volumes - Interlude.mp3
...

```

So, in a directory tree like above, only the tracks inside "Void Of
Vision - Hyperdaze (2019)" would get picked up, and all the "Volumes"
songs wouldn't -- since it wasn't in a subfolder of its own.

As a workaround -- and a necessary cleanup of my music -- I figured I'd
give [beets](https://beets.io) a shot.

## beets

beets is extensively documented, so I'll skip the basics. In essence,
it's a music organization tool -- fetches tags, sorts your collection,
etc. Most of my music has been tagged already, so I skipped that. I only
it all to be grouped by album. A bit of digging in the docs, and I found
what I wanted: `--group-albums`.

And in my `config.yaml`, I specified my desired path format like so:

```yaml
...
paths:
  default: $albumartist - $album%aunique{}/$track $title
```

Finally, running:

```
$ beet import --noautotag --move --group-albums path/to/dirty/music

$ tree ~/music
...

104 directories, 1108 files
```

Nice! gonic then happily scanned all my music.

## actually streaming this music

On my laptop, I decided to just use the NFS share approach -- primarily because
I'd like to stick to `cmus` and desktop Subsonic clients like [Sublime
Music](https://gitlab.com/sublime-music/sublime-music) are very clunky.

On Android, there are quite a few options on F-Droid -- I decided to go with
[Ultrasonic](https://github.com/ultrasonic/ultrasonic) since it's the only one
that supports Last.fm scrobbling.

All things considered, I think I'm pretty satisfied with this. 'twas a good weekend.
