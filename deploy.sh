#!/usr/bin/env bash

echo "[*] Deploying to gh-pages..."
git subtree push --prefix build origin gh-pages
