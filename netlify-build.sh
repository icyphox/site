#!/bin/sh

go get https://github.com/icyphox/go-vite
mkdir build
pip install feedparser arrow python-frontmatter
pip install git+https://github.com/icyphox/myrkdown
go-vite/vite build
