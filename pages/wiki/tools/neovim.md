---
title: neovim
subtitle: Vim, but better.
date: 2021-04-04
template:
---

![neovim](https://x.icyphox.sh/90tj5.png)

Neovim is a drop-in replacement for Vim, with its own excellent
features. The main standout is the ability to [configure it in
Lua](/blog/nvim-lua). This requires Nvim 0.5.0+.

## installing Neovim from source on OpenBSD

Clone https://github.com/neovim/neovim and `cd` into it.
Then,
```
mkdir .deps
cd .deps
cmake ../third-party/
gmake
cd ..
mkdir build
cd build
cmake ..
gmake 
```

Nearly all of my Neovim configs are written in Lua, and are available
at: https://git.icyphox.sh/dotfiles/tree/config/nvim/lua
