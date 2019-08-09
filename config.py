# config.py - Vite's configuration script

title = 'Anirudh'
author = ''
header = """
        <a href="/">home</a>
        <a href="/blog">blog</a>
        <a href="/reading">reading</a>
        <a href="https://twitter.com/icyphox">twitter</a>
        <a href="/about">about</a>
"""
footer = """<a href="https://creativecommons.org/licenses/by-nc-sa/4.0/"><img src="https://licensebuttons.net/l/by-nc-sa/4.0/80x15.png"></a>"""
template = 'index.html'  # default is index.html
post_build = ['./rss.py']
