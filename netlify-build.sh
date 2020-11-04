#!/bin/sh

git clone https://github.com/icyphox/go-vite
cd go-vite && make && cd ..
mkdir build
pip install feedparser arrow python-frontmatter
pip install git+https://github.com/icyphox/myrkdown
go-vite/vite build
