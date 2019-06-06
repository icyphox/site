---
template: text.html
title: Return Oriented Programming on ARM (32-bit)
subtitle: Making stack-based exploitation great again!
date: 05 June, 2019
---

# Return Oriented Programming on ARM (32-bit)
## Making stack-based exploitation great again!

Before we start _anything_, you’re expected to know the basics of ARM
assembly to follow along. I highly recommend
[Azeria’s](https://twitter.com/fox0x01) series on [ARM Assembly
Basics](https://azeria-labs.com/writing-arm-assembly-part-1/). Once you’re
comfortable with it, proceed with the next bit — environment setup.

### Setup

Since we’re working with the ARM architecture, there are two options to go
forth with: 

1. Emulate — head over to [qemu.org/download](https://www.qemu.org/download/) and install QEMU. 
And then download and extract the ARMv6 Debian Stretch image from one of the links [here](https://blahcat.github.io/qemu/).
The scripts found inside should be self-explanatory.
2. Use actual ARM hardware, like an RPi.

For debugging and disassembling, we’ll be using plain old `gdb`, but you
may use `radare2`, IDA or anything else, really. All of which can be
trivially installed.

Finally, the binary we’ll be using in this exercise is [Billy Ellis’](https://twitter.com/bellis1000)
[roplevel2](/static/files/roplevel2.c). 

Compile it:
```sh
$ gcc roplevel2.c -o rop2
```

With that out of the way, here’s a quick run down of what ROP actually is.

### A primer on ROP

ROP or Return Oriented Programming is a modern exploitation technique that’s
used to bypass protections like the **NX bit** (no-execute bit) and **code sigining**.
In essence, no code in the binary is actually modified and the entire exploit
is crafted out of pre-existing artifacts within the binary, known as **gadgets**.

A gadget is essentially a small sequence of code (instructions), ending with
a `ret`, or a return instruction. In our case, since we’re dealing with ARM
code, there is no `ret` instruction but rather a `pop {pc}` or a `bx lr`.
These gadgets are _chained_ together by jumping (returning) from one onto the other
to form what’s called as a **ropchain**. At the end of a ropchain,
there’s generally a call to `system()`, to acheive code execution.

In practice, the process of executing a ropchain is something like this:

- confirm the existence of a stack-based buffer overflow
- identify the offset at which the instruction pointer gets overwritten
- locate the addresses of the gadgets you wish to use
- craft your input keeping in mind the stack’s layout, and chain the addresses
of your gadgets

[LiveOverflow](https://twitter.com/LiveOverflow) has a [beautiful video](https://www.youtube.com/watch?v=zaQVNM3or7k&list=PLhixgUqwRTjxglIswKp9mpkfPNfHkzyeN&index=46&t=0s) where he explains ROP using “weird machines”. 
Check it out, it might be just what you needed for that “aha!” moment :)

Still don’t get it? Don’t fret, we’ll look at _actual_ exploit code in a bit and hopefully
that should put things into perspective.

### Exploring our binary

Start by running it, and entering any arbitrary string. On entering a fairly
large string, say, “AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA”, we
see a segmentation fault occur.

![string and segfault](/static/img/string_segfault.png)

Now, open it up in `gdb` and look at the functions inside it.

![gdb functions](/static/img/gdb_functions.png)

There are three functions that are of importance here, `main`, `winner` and 
`gadget`. Disassembling the `main` function:

![gdb main disassembly](/static/img/gdb_main_disas.png)

We see a buffer of 16 bytes being created (`sub	sp, sp, #16`), and some calls
to `puts()`/`printf()` and `scanf()`. Looks like `winner` and `gadget` are 
never actually called.

Disassembling the `gadget` function:

![gdb gadget disassembly](/static/img/gdb_gadget_disas.png)

This is fairly simple, the stack is being initialized by `push`ing `{r11}`,
which is also the frame pointer (`fp`). What’s interesting is the `pop {r0, pc}`
instruction in the middle. This is a **gadget**.

We can use this to control what goes into `r0` and `pc`. Unlike in x86 where
arguments to functions are passed on the stack, in ARM the registers `r0` to `r3`
are used for this. So this gadget effectively allows us to pass arguments to
functions using `r0`, and subsequently jumping to them by passing its address
in `pc`. Neat.

Moving on to the disassembly of the `winner` function:

![gdb winner disassembly](/static/img/gdb_disas_winner.png)




