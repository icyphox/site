#!/bin/sh

pip install git+https://github.com/icyphox/vite
mkdir build
pip install feedparser arrow
vite build
