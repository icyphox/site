# config.py - Vite's configuration script

title = "icyphox"
author = ""
header = """<a href="/"><- back</a>"""

# actually the sidebar
footer = """
    <img class="logo" src="/static/icyphox.png" alt="icyphox's avatar" />
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
    <span class="sidebar-link">mastodon</span>
    <br>
      <a rel="me" href="https://freeradical.zone/@icyphox">@icyphox@freeradical.zone</a>
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

    <div class="license">
    <a href="https://liberapay.com/icyphox/donate">
    <img alt="Donate using Liberapay" src="https://liberapay.com/assets/widgets/donate.svg">
    </a>
    <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
    <img class="footimgs" src="/static/cc.svg">
    </a>
    <a href="https://webring.xxiivv.com/#random" target="_blank">
    <img class="footimgs" alt="xxiivv webring" src="/static/webring.svg">
    </a>
    </div>
        """
template = 'text.html'  # default is index.html
pre_build = [['./bin/openring.py', '-j'], './bin/update_index.py']
post_build = ['./bin/rss.py', './bin/plaintext.sh', './bin/acme.sh']
