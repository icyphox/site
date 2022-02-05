#!/bin/sh

python3 -m http.server --directory build &> /dev/null
find pages/ | entr vite build
