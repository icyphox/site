#!/usr/bin/env bash

echo "[*] Deploying to gh-pages..."
git subtree push --prefix build origin gh-pages
echo "[*] Done! Check it out at: https://icy.ph0x.me"
