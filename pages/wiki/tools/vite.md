---
title: vite
subtitle: A minimal and fast static site generator written in Go.
date: 2021-03-27
template: page.html
---

This site is built using [vite](https://git.icyphox.sh/vite). This is
vite, the 2nd. Its predecessor,
[py-vite](https://git.icyphox.sh/py-vite) was a Python program. It was
also the first ever "tool" I wrote for myself, back in early 2018.
Ironically, it was far from _vite_, with builds taking upwards of 10
seconds at times.

vite's primary goals are:

- speed
- extensibility -- the ability to run commands before and after a build
- minimalism

It is configured via a `config.yaml` file present in the site's root.
Consult the readme for more info.

vite is available under the MIT license.
