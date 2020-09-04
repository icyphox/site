# config.py - Vite's configuration script

title = "icyphox"
author = ""
header = ""

# actually the sidebar
footer = f"""
    <img class="logo" src="/static/white.svg" alt="icyphox's avatar" style="width: 55%"/>
    <p>
    <span class="sidebar-link">email</span>
    <br>
      <a href="mailto:x@icyphox.sh">x@icyphox.sh</a>
    </p> 

    <p>
    <span class="sidebar-link">github</span>
        <br>
      <a href="https://github.com/icyphox">icyphox</a>
    </p> 

    <p>
    <span class="sidebar-link">fediverse</span>
    <br>
    <a rel="me" href="https://toot.icyphox.sh/@x">@x@toot.icyphox.sh</a>
    </p> 

    <p>
    <span class="sidebar-link">pgp</span>
    <br>
      <a href="/static/gpg.txt">0x8A93F96F78C5D4C4</a>
    </p> 

    <h3>friends</h3>
    <p>
    Some of <a href="/friends">my friends</a> and internet bros.
    </p>

    <h3>about</h3>
    <p>
    More <a href="/about">about me</a> and my work.
    </p>

    <div class="icons">
    <a href="https://creativecommons.org/licensjes/by-nc-sa/4.0/">
    <img class="footimgs" alt="cc nc-by-sa" src="/static/cc.svg">
    </a>
    <a href="https://webring.xxiivv.com/#random" target="_blank">
    <img class="footimgs" alt="xxiivv webring" src="/static/webring.svg">
    </a>
    <a href="/blog/feed.xml" >
    <img class="footimgs" alt="rss feed" src="/static/rss.svg">
    </a>
    </div>

        """
template = 'text.html'  # default is index.html
pre_build = ['bin/update_index.py']
post_build = ['bin/rss.py', 'bin/plaintext.sh']
