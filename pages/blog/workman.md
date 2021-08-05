---
template:
slug: workman
title: The Workman keyboard layout
subtitle: I have a lot of free time on my hands (heh)
date: 2020-10-24
---

I've been at my computer everyday, for at least 10 hours at minimum.
These past ~6 - 7 months have been the most I've ever used my computer.
Eventually, I started experiencing discomfort and pain -- especially in
my pinkie finger. Typing became a chore, and I found myself using my
shell's command history more just to avoid typing commands. I tried
using a wrist rest, different keyboard heights, but nothing helped.

Thus began my search for a new keyboard layout, and it swiftly concluded
once I chanced upon the [Workman layout](https://workmanlayout.org).
According to the website, it is supposedly an improvement over Colemak
and Dvorak. I skimmed through the numbers and other stats, but
I honestly didn't care. "Oh it's better than the popular alternative
layouts? Okay that's enough for me."

![workman layout](https://raw.githubusercontent.com/kdeloach/workman/gh-pages/images/workman_layout.png)

I downloaded the tarball containing the different config files for
different platforms etc. I just needed the `xmodmap` -- that's the
easiest way to apply a keyboard layout.

```console
$ xmodmap xmodmap.workman
```

To practice the layout, I used [keybr.com](https://keybr.com). You can
configure the keyboard layout via the settings. Naturally, the first few
days were incredibly painful. I was only able to type short sentences
with very small words. I tried to not engage in heated discussions on
IRC, for I could not type up a response in time. However, if I did
stumble into one, I would switch back to QWERTY just for those couple of
messages.

I found myself making the switch less and less, over the next few days.
Chatting on IRC is a _great_ way to learn a layout. Or chatting
anywhere, really. It forces you to get accustomed to the layout by
typing the common words used in conversation. I also made a tiny change
to the layout -- swapping the <kbd>F</kbd> and <kbd>B</kbd> keys, since
typing the "fo" / "of" digram in the same hand felt really weird. Soon
enough, I was averaging about 30 - 40 WPM within the first week of
having switched to Workman. 

And then things at work started to pick up, and I had to do what I had
been dreading the most: edit code -- in Vim. It's fairly common
knowledge that Vim, by default, extensively uses the <kbd>H</kbd>,
<kbd>J</kbd>, <kbd>K</kbd> and <kbd>L</kbd> keys for navigation. Sure,
there are better ways to move around and only using those keys is
frowned upon -- but it's a habit built over years, and hard to shake
off. After poking around for a bit, I found the
[vim-workman](https://github.com/nicwest/vim-workman) plugin. Forked it
to apply the <kbd>F</kbd>/<kbd>B</kbd> change, and I began using it.

It was great at first. My Vim muscle memory was not hampered, as I was
able to use QWERTY in normal mode, and Workman in insert. But as I got
better at Workman, I found myself instinctively reaching for the Workman
keys in normal mode. Well, everything except for the <kbd>H</kbd>,
<kbd>J</kbd>, <kbd>K</kbd> and <kbd>L</kbd> keys. This quickly became
bothersome and I uninstalled the plugin to search for a better solution.

Wait, don't I have a sick new [programmable mechanical
keyboard](/blog/ducky-one-2)? What if I configure a layer on it just for the
<kbd>H</kbd>, <kbd>J</kbd>, <kbd>K</kbd>, <kbd>L</kbd> keys? After pouring
through the manual for a bit, I eventually got it set up. I even remapped
the <kbd>Caps Lock</kbd> key to <kbd>Fn</kbd> so it's easier to access the
layer. So now, hitting <kbd>Caps
Lock</kbd>+<kbd>Y</kbd>/<kbd>N</kbd>/<kbd>E</kbd>/<kbd>O</kbd> results in
<kbd>HJKL</kbd> being pressed. This took a little bit of getting used to,
but it got easier with a bit of practice. 

Since I don't rely on any plugin/remappings, I can use Vim as is on
remote machines too. Another bonus from this adventure was I actually
spent time learning better ways to navigate, and reduce my reliance on
<kbd>HJKL</kbd>. Overall, a big win.

It's been over 4 weeks since my switch, I think, and I'm comfortably
averaging around 80 WPM. Still a good 20 WPM slower than QWERTY, but
I think it'll get better with time. And am I still able to use QWERTY?
Well, kinda. I still use QWERTY on my phone keyboard, since Workman
isn't an option on it and it's actually alright. However, when I use my
desktop to play Dota, I prefer using voice chat to communicate since
typing on QWERTY takes too long -- I am forced to hunt and peck.
Interestingly, after about 15 - 20 minutes on QWERTY, my brain kinda
just clicks back and I can type on it with relative ease. Not as fast as
I used to be, but it's manageable.

All things considered, switching to Workman was one of the better
decisions I have made in life. It feels so nice to be able to type out
whole words in just the home row. It just _flows_ so nicely, and it has
made typing so much more enjoyable again.
