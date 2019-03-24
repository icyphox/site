#!/usr/bin/env bash

# build, because i never do
vite build

# push contents of `build/` to the `gh-pages` branch
git subtree push --prefix build origin gh-pages
