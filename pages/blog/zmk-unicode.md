---
template:
slug: zmk-unicode
title: Unicode text input in ZMK
subtitle: A hacky interim solution using macros
date: 2022-10-18
---

As a highly cultured em-dash (over-)user, being able to type '—' easily
is very important to me. While waiting for
[zmkfirmware/zmk#232](https://github.com/zmkfirmware/zmk/issues/232) to
get merged, I've discovered a rather nifty workaround for inputting
Unicode text. This method makes use of
[IBus](https://github.com/ibus/ibus) and a ZMK macro.

Unicode input in IBus is done by typing `Ctrl` + `Shift` + `U` followed
by the Unicode codepoint and then a `Space` or `Return`. Writing this
as a ZMK macro, we get something like:

```dts
macros {
    uc_dash: uc_dash {
        label = "UNICODE_DASH";
        compatible = "zmk,behavior-macro";
        #binding-cells = <0>;
        tap-ms = <0>;
        wait-ms = <0>;
        bindings
            = <&macro_press &kp LCTRL &kp LSHFT>
            , <&macro_tap &kp U>
            , <&macro_release &kp LCTRL &kp LSHFT>
            , <&macro_tap &kp N2 &kp N0 &kp N1 &kp N4 &kp SPC>
            ;
    }; 
};
```

Where the numbers `2014` denote the codepoint for an em-dash. Set the
`wait-ms` and the `tap-ms` to `0` to make it instantaneous -- your
keyboard will essentially type out the entire key combo really fast. The
resulting keycode `uc_dash` can be used in any `bindings` field. I have
it on a separate Unicode layer.

The unfortunate caveat is it only works where IBus works, and it doesn't
seem to work in Qt applications. Granted, I only really need it in my
browser and Signal/Slack Desktop (Electron) so that isn't a dealbreaker.

My ZMK config is [here](https://github.com/icyphox/ferricy-zmk).
