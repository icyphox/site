# Break the Ice — Hardware CTF

## SecureLayer7’s hardware CTF at Nullcon ’19, Goa

Earlier this month at Nullcon Goa, we had the chance to attempt a hardware CTF challenge designed by the folks at [SecureLayer7](https://securelayer7.net). We weren’t able to solve it during the period of 2 days that we had (we had talks and parties to be at), but the SL7 guys were kind enough to let us keep the hardware and solve it back at home. Which we did, otherwise this write-up wouldn’t have happened :)

### The Hardware

So what’s this cryptic “hardware” I keep mentioning, you wonder? It’s an ESP8266 board — better known as a **NodeMCU**. Here’s a picture.

![](1*cWpvtbXan4LjdJBldelW-g.jpeg)

Oh, and it came with a pretty OLED display too. So the obvious task at hand was to connect the display to the board. A quick search, and we found an (ever helpful) [Instructables](https://www.instructables.com/id/Interface-LCD-Using-NodeMCU/) link with the image down below.

![Not the same display, but it works](1*1avLAYsHDTGU-JS3e6oVrA.jpeg)*Not the same display, but it works*

Mind you, we struggled quite a bit at this seemingly trivial step, but hey we’re CS students ;)

On connecting the device via USB, the board spins up a wireless hotspot called “Device-6”.

![](1*wJ3ZY2EskoSSfvCjliP_jQ.png)

We tried to connect to this, but it was password protected. We’ll get back to it later.

### Flash dump analysis

During one of the many web searches I made with regard to this board, an interesting tool showed up — [esptool](https://github.com/espressif/esptool). A Python utility to communicate with the ESP8266. Wonderful.

This tool allows us to do a bunch of operations on the board, but what we’re actually interested in is reading the flash. After looking up the syntax for it, we arrived at:

```
› sudo ./esptool.py -p /dev/ttyUSB0 -b 460800 read_flash 0 0x400000 flash_contents.bin
Serial port /dev/ttyUSB0
Connecting....
Detecting chip type... ESP8266
Chip is ESP8266EX
Features: WiFi
MAC: 84:f3:eb:05:83:1e
Uploading stub...
Running stub...
Stub running...
Changing baud rate to 460800
Changed.
4194304 (100 %)
4194304 (100 %)
Read 4194304 bytes at 0x0 in 100.8 seconds (333.0 kbit/s)...
Hard resetting via RTS pin...
```


The command is fairly easy to understand, the `-p` flag denotes the serial port of our device, `-b` specifies the Baud rate and `read_flash`, well, reads the flash starting at `0` till `0x400000` which is 4MB. 
We faced a lot of trouble here, since we kept reading only upto 2MB. Why? Because that’s what the command on the Internet said.

Anyway, we have our flash dumped into a file `flash_contents.bin`.

We then decided to run `strings` on the flash binary and peruse through the thousands of lines it had. Brilliant right? It was, actually. We found a bunch of interesting strings, along with what we guessed to be the wireless hotspot’s password. Spoiler alert: it was.

![The entire dump was 6000+ lines. Did we actually do this D:](1*5Hc-_XYFw-4_hw3iZpfqkQ.png)*The entire dump was 6000+ lines. Did we actually do this D:*

The go-to utility to (actually) analyze binaries is `binwalk`. The `-e` flag extracts the known file types it recognizes within the binary.

```
› binwalk -e flash_contents.bin

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
283960        0x45538         Unix path: /root/.arduino15/packages/esp8266/hardware/esp8266/2.5.0/libraries/ESP8266WiFi/src/include/DataSource.h
289387        0x46A6B         HTML document footer
291156        0x47154         HTML document header
291296        0x471E0         Unix path: /root/.arduino15/packages/esp8266/hardware/esp8266/2.5.0/cores/esp8266/abi.cpp
3145728       0x300000        Squashfs filesystem, little endian, version 4.0, compression:gzip, size: 139733 bytes, 10 inodes, blocksize: 131072 bytes, created: 2019-02-25 09:14:19
```


We see a squashfs filesystem here. `binwalk` creates a directory in your current path containing all the files and folders it managed to extract. `cd`ing into our squashfs folder, we see this:

![:O](1*VsEzd8PSYMIUwjBLNFFetA.png)*:O*

Oooh yes. `cat`ting the file, we see:

```
› cat 1/Hidden.txt

######################################### Hints :) ########################################

---telnet server on esp

--Hunt the key to get MQTT creds
          -- 
--MQTT box

--Publish the correct message to get ^FLAG^

<<<<<<<<<<<<<<<<     PUBLISH..... DISPLAY.... SUBMIT.... :)  >>>>>>>>>>>>>>>>>>>>>>
```


Looking inside the directory named `2`, we see another dir `3` containing a JPEG image and a file telling us about steganography.

![](1*68k1Y6IoK0XTCPTQRn_0fw.png)

And the final directory `4` had nothing in it but a file with the string `flag`. Probably to show up as a false positive in the `strings` output of the flash dump.

### Connecting to “Device-6”

The first file we came across, containing the hints, mentioned a `telnet` server running on the board. But how do we reach it? Yep, via the wireless hotspot it exposes — “Device-6”. We authenticated using the PSK we found earlier. 
On doing so, we’re prompted with a captive portal:

![](1*XelmAgITUw-9aZc26meUDQ.png)

A few things can be done here, configure WiFi on the board, view some info about the board, and reset it. Let’s connect the ESP to our own SSID — like a mobile hotstpot.

![](1*oQcTNKOFGphPbX50K2pmlg.png)

Once that’s done, we should see the “Device-6” SSID disappear, indicating that the board is now connected to our own wireless hotstpot. Another thing we notice is the board lights up, and so does our display!

![That’s so sad. Alexa play Despacito.](1*lzKOxEkzJqo8TNI4WckmOg.png)*That’s so sad. Alexa play Despacito.*

### The telnet server

Once our host machine and the ESP are on the same network, we can `nmap` our subnet to find our ESP’s IP.

![nmap scan report](1*lPNqoIFmNfxfabdt4sqYSQ.png)*nmap scan report*

We see an `http` server running, which was obviously the captive portal, and our `telnet` server on port 23.

```
› telnet 192.168.43.223
Trying 192.168.43.223...
Connected to 192.168.43.223.
Escape character is '^]'.
Press Enter & sumbit your key :)
somekey
Wrong Key!!!
```


On connecting, we see a prompt asking for a key. And no, ‘sumbit’ was spelt that way ;)

Where could this key possibly be? Well, the only unexplored part of this CTF so far is the image file we came across before. So… steganography.

Although you won’t need it, I downloaded this Docker image for cracking stego — [stego-toolkit](https://hub.docker.com/r/dominicbreuker/stego-toolkit/). We then tossed the image under a bunch of steganography detection and breaking tools, but to no avail.

After a good while `steghide` gave us something:

```
› steghide extract -sf 10071856.jpg            
Enter passphrase:
```


This took *really* long for us to figure but the password was the name of the image file itself. Urgh. On entering the password, we get a `keys.txt` file. Here’s what it looked like:

```
So you guessed the password i think...

Nice!!!

Key is somewhere hidden in this strings ...

XH}<
TJJ*
Y#pU
<g?/N
gr[i}5
>+h1
...snip...
jlW8B
yjbm
M4%'
tx;ZzL
3 k]
wPUf'rc
)Pz#
0AwN\
Lgr:J2
!H9u
4bSVy
(*-C
nOf2E\

Aaaaaand key is not guessable ....

WARNING:Manual checking for correct key might take you 2 days to complete the challange!!
```


Nearly 600 lines of gibberish. We guessed that one of these strings had to be they key for our `telnet` session. We tried to automate it, but the `telnet` session was very unstable. So being the madmen we were, we did it manually. We had all the time in the world. Off we went, copy/pasting the keys in batches of 5… and it worked.

![yeet](1*vY84DrSpJU1H4c9pSvoB5Q.png)*yeet*

As the hint file mentioned, we had to connect to an MQTT instance somewhere and publish something for the flag. So this is what they were talking about.

For those out-of-the-loop, [MQTT](https://en.wikipedia.org/wiki/MQTT) is the protocol used in IoT basec client-server interactions, among other things. Go read about it if you want to understand the next bit.

### Capturing the flag

To interact with the MQTT server, we’ll be using the [Mosquitto](https://mosquitto.org) client. We then use the credentials and attempt to “publish” a message:

```
› mosquitto_pub -h 'm16.cloudmqtt.com' -p 17551  -t 'inTopic/web/test' -u 'hchzbuhr' -P 'Sz4plHnlVnHc' -m '(^.^)'
```


![UwU](1*W_iVf3vDf4UaelycMbvPvw.png)*UwU*

After messing around with this for quite a bit (as is evident from the screen behind), we tried sending the string ‘flag’ as our message and… *dramatic pause* we got what you’d expect.

![We were 10 days late, mind you](1*sO9vDtGgGjejxklF46gTlg.jpeg)*We were 10 days late, mind you*

### Conclusion

This was our first time playing a hardware CTF, and to be honest, there wasn’t *much *of “hacking” involved — at least by the word’s textbook definition. A lot of guesswork too, which made some parts of it excruciatingly painful to figure out. But all things considered, it was probably the most fun CTF I’ve played yet. Here’s a shoutout to the folks at SL7 for making this CTF *and* letting us keep the ESP :)

That’s it. The end.
