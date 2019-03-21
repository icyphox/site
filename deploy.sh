#!/usr/bin/env bash

# push contents of `build/` to the `gh-pages` branch
git subtree push --prefix build origin gh-pages
