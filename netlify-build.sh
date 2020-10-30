#!/bin/sh

go get https://github.com/icyphox/go-vite
mkdir build
pip install feedparser arrow python-frontmatter
go-vite/vite build
