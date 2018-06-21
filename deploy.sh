#!/usr/bin/env bash

# colors
ylw='\033[0;33m'
grn='\033[0;32m'
rst='\033[0m'

echo -e "$ylw[~]$rst Deploying to gh-pages..."
git subtree push --prefix build origin gh-pages
echo -e "$grn[+]$rst Done! Check it out at: https://icy.ph0x.me"
