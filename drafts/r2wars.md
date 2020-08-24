---
template:
url: r2wars
title: My r2wars attempts
subtitle: It's like Killer Robots, except in assembly
date: 2020-08-17
---

[r2wars](https://github.com/radareorg/r2wars) is
a [CoreWar](http://corewars.org)-like game thar runs within the radare2
[ESIL](https://radare.gitbooks.io/radare2book/content/disassembling/esil.html)
virtual machine. In short, you have two programs running in a shared
memory space (1kb), with the goal of killing the other and surviving as
long as possible. You're allowed to write your bots in x86, ARM and MIPS
(32 and 64 bits).

I'd initially considered writing my bots in ARM -- but x86's `pushad`
won me over. And I didn't really feel like revising my ARM... maybe
I should. We'll see. 

## `bomb.x86-32.asm`

This was the first bot I wrote. It's incredibly simple -- it carpet
bombs the entire address space (`0x000` - `0x400`) with 
