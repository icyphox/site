---
template:
slug: nvim-lua
title: Configuring Neovim using Lua
subtitle: And switching from init.vim to init.lua
date: 2021-02-07
---

If you, like me, never really understood Vimscript and hate the language
with a passion, you're in the right place! You can now get rid of
Vimscript wholesale and replace it with a simpler, faster and elegant-er
language -- Lua! _However_, this is only possible from Neovim 0.5
onwards[^1] and as of now, requires you to install Neovim from HEAD. How
to do that is left as an exercise to the reader. Also bear in mind that
the Lua API is fairly beta right now, and many Vim things don't have
direct interfaces.

[^1]: https://github.com/neovim/neovim/pull/12235

So assuming you're now running Neovim `master`, head over to
`~/.config/nvim` and create your `init.lua`. Why, yes, we're porting
over your `init.vim` to `init.lua` right now! Clear your calendar for
the next few hours -- bikeshedding your text editor is top priority!

I also recommend going through
[nanotee/nvim-lua-guide](https://github.com/nanotee/nvim-lua-guide)
and [Learn Lua in Y minutes](https://learnxinyminutes.com/docs/lua/)
before starting off.

## the directory structure

Lua files are typically under `~/.config/nvim/lua`, and can be loaded as
Lua modules. This is incredibly powerful -- you can structure your
configs however you like. 

```console
$ tree .config/nvim
.
|-- ftplugin
|   `-- ...
|-- init.lua
|-- lua
|   |-- maps.lua
|   |-- settings.lua
|   |-- statusline.lua
|   `-- utils.lua
`-- plugin
    `-- ...
```

The common approach is to have different
bits of your config in Lua files under `lua/` and `require`'d in your
`init.lua`, so something like:

```lua
-- init.lua

require('settings')    -- lua/settings.lua
require('maps')        -- lua/maps.lua
require('statusline')  -- lua/statusline.lua
```

## the basics: setting options

Vim has 3 kinds of options -- global, buffer-local and window-local. In
Vimscript, you'd just `set` these. In Lua, however, you will have to
use one of

- `vim.api.nvim_set_option()` -- global options
- `vim.api.nvim_buf_set_option()` -- buffer-local options
- `vim.api.nvim_win_set_option()` -- window-local options

These are fairly verbose and very clunky, but fortunately for us, we
have "meta-accesors" for these: `vim.{o,wo,bo}`. Here's an excerpt from
my `settings.lua` as an example:

```lua
local o = vim.o
local wo = vim.wo
local bo = vim.bo

-- global options
o.swapfile = true
o.dir = '/tmp'
o.smartcase = true
o.laststatus = 2
o.hlsearch = true
o.incsearch = true
o.ignorecase = true
o.scrolloff = 12
-- ... snip ... 

-- window-local options
wo.number = false
wo.wrap = false

-- buffer-local options
bo.expandtab = true
```

If you're not sure if an option is global, buffer or window-local,
consult the Vim help! For example, `:h 'number'`:

```
'number' 'nu'           boolean (default off)
                        local to window
```

Also note that you don't set the negation of an option to true, like
`wo.nonumber = true`, you instead set `wo.number = false`.

## defining autocommands

Unfortunately, autocommands in Vim don't have a Lua interface -- it is
being worked on.[^2] Until then, you will have to use
`vim.api.nvim_command()`, or the shorter `vim.cmd()`. I've defined a
simple function that takes a Lua table of `autocmd`s as an argument, and
creates an `augroup` for you.

```lua
-- utils.lua

local M = {}
local cmd = vim.cmd

function M.create_augroup(autocmds, name)
    cmd('augroup ' .. name)
    cmd('autocmd!')
    for _, autocmd in ipairs(autocmds) do
        cmd('autocmd ' .. table.concat(autocmd, ' '))
    end
    cmd('augroup END')
end

return M

-- settings.lua
local cmd = vim.cmd
local u = require('utils')

u.create_augroup({
    { 'BufRead,BufNewFile', '/tmp/nail-*', 'setlocal', 'ft=mail' },
    { 'BufRead,BufNewFile', '*s-nail-*', 'setlocal', 'ft=mail' },
}, 'ftmail')

cmd('au BufNewFile,BufRead * if &ft == "" | set ft=text | endif')
```

[^2]: https://github.com/neovim/neovim/pull/12378

## defining keymaps

Keymaps can be set via `vim.api.nvim_set_keymap()`. It takes 4
arguments: the mode for which the mapping will take effect, the key
sequence, the command to execute and a table of options (`:h
:map-arguments`).

```lua
-- maps.lua

local map = vim.api.nvim_set_keymap

-- map the leader key
map('n', '<Space>', '', {})
vim.g.mapleader = ' '  -- 'vim.g' sets global variables


options = { noremap = true }
map('n', '<leader><esc>', ':nohlsearch<cr>', options)
map('n', '<leader>n', ':bnext<cr>', options)
map('n', '<leader>p', ':bprev<cr>', options)
```

For user defined commands, you're going to have to go the `vim.cmd`
route:

```lua
local cmd = vim.cmd

cmd(':command! WQ wq')
cmd(':command! WQ wq')
cmd(':command! Wq wq')
cmd(':command! Wqa wqa')
cmd(':command! W w')
cmd(':command! Q q')
```

## managing packages

Naturally, you can't use your favourite Vimscript package manager
anymore, or at least, not without `vim.api.nvim_exec`ing a bunch of
Vimscript (ew!). Thankfully, there are a few pure-Lua plugin managers
available to use[^3] -- I personally use, and recommend
[paq](https://github.com/savq/paq-nvim/). It's light and makes use of
the [`vim.loop`](https://docs.libuv.org/en/v1.x/) API for async I/O.
paq's docs are plentiful, so I'll skip talking about how to set it up.

[^3]: Also see: [packer.nvim](https://github.com/wbthomason/packer.nvim/)

## bonus: writing your own statusline

Imagine using a bloated, third-party statusline, when you can just write
your own.[^4] It's actually quite simple! Start by defining a table for
every mode:

[^4]: This meme was made by NIH gang.

```lua
-- statusline.lua

 local mode_map = {
	['n'] = 'normal ',
	['no'] = 'n·operator pending ',
	['v'] = 'visual ',
	['V'] = 'v·line ',
	[''] = 'v·block ',
	['s'] = 'select ',
	['S'] = 's·line ',
	[''] = 's·block ',
	['i'] = 'insert ',
	['R'] = 'replace ',
	['Rv'] = 'v·replace ',
	['c'] = 'command ',
	['cv'] = 'vim ex ',
	['ce'] = 'ex ',
	['r'] = 'prompt ',
	['rm'] = 'more ',
	['r?'] = 'confirm ',
	['!'] = 'shell ',
	['t'] = 'terminal '
}
```

The idea is to get the current mode from `vim.api.nvim_get_mode()` and
map it to our desired text. Let's wrap that around in a small `mode()`
function:

```lua
-- statusline.lua

local function mode()
	local m = vim.api.nvim_get_mode().mode
	if mode_map[m] == nil then return m end
	return mode_map[m]
end
```

Now, set up your highlights. Again, there isn't any interface for
highlights yet, so whip out that `vim.api.nvim_exec()`.

```lua
-- statusline.lua

vim.api.nvim_exec(
[[
  hi PrimaryBlock   ctermfg=06 ctermbg=00
  hi SecondaryBlock ctermfg=08 ctermbg=00
  hi Blanks   ctermfg=07 ctermbg=00
]], false)
```

Create a new table to represent the entire statusline itself. You can
add any other functions you want (like one that returns the current git
branch, for instance). Read `:h 'statusline'` if you don't understand
what's going on here.

```lua
-- statusline.lua

local stl = {
  '%#PrimaryBlock#',
  mode(),
  '%#SecondaryBlock#',
  '%#Blanks#',
  '%f',
  '%m',
  '%=',
  '%#SecondaryBlock#',
  '%l,%c ',
  '%#PrimaryBlock#',
  '%{&filetype}',
}
```

Finally, with the power of `table.concat()`, set your statusline. This
is akin to doing a series of string concatenations, but way faster.

```lua
-- statusline.lua

vim.o.statusline = table.concat(stl)
```

![statusline](https://cdn.icyphox.sh/statusline.png)

## this is what being tpope feels like

You can now write that plugin you always wished for! I sat down to write
a plugin for [fzy](https://github.com/jhawthorn/fzy)[^5], which you can
find [here](https://git.icyphox.sh/dotfiles/tree/config/nvim/lua/fzy)
along with my entire Neovim config[^6]. I plan to port a the last of my
`plugin/` directory over to Lua, soon™.

And it's only going to get better when the Lua API is completed. We can
all be Vim plugin artists now.

[^5]: A less bloated alternative to fzf, written in C.
[^6]: [GitHub link](https://github.com/icyphox/dotfiles/tree/master/config/nvim) --
      if you're into that sort of thing.
