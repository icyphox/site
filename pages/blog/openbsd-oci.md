---
template:
slug: openbsd-oci
title: Installing OpenBSD on Oracle Cloud
subtitle: It finally works in 7.2!
date: 2022-11-24
---

I've been trying to get OpenBSD to install on OCI since [early last
year](https://marc.info/?l=openbsd-misc&m=162962869305286&w=2). As
described in my email to misc@, my intial method of installation was
rather unconventional:

- Download the install image to tmpfs
- dd it onto the host boot device (/dev/sda)
- Reboot

This works perfectly for Alpine, I'll have you know but not so much for
OpenBSD. I don't know why. Anyway, with that rather useless preface
aside, [OpenBSD now supports](https://openbsd.org/72.html) booting on
amd64 OCI instances:

> Allowed bsd.rd and bsd/bsd.mp to boot on Oracle Cloud amd64 instances.

This time around, I decided to try a somewhat less nuclear approach to
booting it. The steps I followed were from a kind [internet stranger's
article](https://blinken.life/oci-obsd/), coincedentally ranting about
how they _failed_ to boot OpenBSD on OCI.[^1]

[^1]: I pinged them on the fedi to let them know it works now: https://h.icyphox.sh/u/icy/h/3NGd59X2d6Kr958Nt2

It's fairly straight forward, and you'll be fine simply following the
steps in the article I linked above; but since you're here, let's run
through them real quick:

1. Download the `install72.img` onto an OpenBSD machine. Trust me,
   dealing with loopback mounts is not fun on Linux.

2. "Mount" the install image using [vnconfig(8)](https://man.openbsd.org/vnconfig):
    ```
    vnconfig vnd0 install72.img
    mount /dev/vnd0a /mnt
    ```
3. Configure booting over serial:
    ```
    echo 'set tty com0' > /mnt/etc/boot.conf
    ```
4. Convert the modified `install72.img` to qcow2 using `qemu-img`. We
   will be uploading this to OCI as a custom image.
   ```
   qemu-img convert -O qcow2 install72.img install.qcow2
   ```

5. Uploading the image requires creating an object storage bucket first.
   Navigate to Storage → Buckets and create one. Call it whatever.

6. Upload the qcow2 from step 4.

7. Head to Compute → Custom Images and click Import Image. Choose your
   bucket and qcow2 and select image type as QCOW2. We'll stick to
   Paravirtualized mode. Give it a bit.

8. Once it's done importing, create a new amd64 instance like you
   normally would, and choose your newly created custom image. Don't
   bother with SSH keys.

9. Launch a console connection to access the serial boot. You should
   hopefully see the OpenBSD installer. You might have to hit Enter
   once. Hit 'I' and start the install.

10. There should only be one disk available. Choose that. Everything
    else should just work like in any other OpenBSD install.

That's about it. I for one am super excited to move all my instances to
OpenBSD. As always, [donate to the OpenBSD
project](https://www.openbsd.org/donations.html) to ensure the continued
development of our beloved puffy.
