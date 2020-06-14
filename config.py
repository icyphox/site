# config.py - Vite's configuration script

title = "icyphox"
author = ""
header = """<a href="/"><- back</a>"""

# gets the latest commit 
import subprocess

def get_commit():
    out = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"], 
            stdout=subprocess.PIPE)
    commit = out.stdout.decode("utf-8").strip()
    return commit

def get_big_commit():
    out = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            stdout=subprocess.PIPE
            )
    big_commit = out.stdout.decode("utf-8").strip()
    return big_commit


def get_commit_date(commit):
    out = subprocess.run(
            ["git", "show", "-s", "--format=%cd", "--date=short", commit],
            stdout=subprocess.PIPE)
    date = out.stdout.decode("utf-8").strip()
    return date

commit = get_commit()
big_commit = get_big_commit()
date = get_commit_date(commit)

# actually the sidebar
footer = f"""
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
    <a rel="me" href="https://toot.icyphox.sh/@x">@x@icyphox.sh</a>
    </p> 

    <p>
    <span class="sidebar-link">pgp</span>
    <br>
      <a href="/static/gpg.txt">0x8A93F96F78C5D4C4</a>
    </p> 

    <p>
    <span class="sidebar-link">last updated</span>
    <br>
    <a href="https://github.com/icyphox/site/commit/{big_commit}">{commit}</a> on {date}
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
    <img class="footimgs" src="/static/cc.svg">
    </a>
    <a href="https://webring.xxiivv.com/#random" target="_blank">
    <img class="footimgs" alt="xxiivv webring" src="/static/webring.svg">
    </a>
    </div>

        """
template = 'text.html'  # default is index.html
pre_build = [['bin/openring.py', '-j'], 'bin/update_index.py']
post_build = ['bin/rss.py', 'bin/plaintext.sh']
