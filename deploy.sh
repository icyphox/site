#!/usr/bin/env bash

git push origin master
# push contents of `build/` to the `gh-pages` branch
git subtree push --prefix build origin gh-pages
