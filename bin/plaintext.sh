#!/bin/sh 

# from the pure sh bible; see: 
# https://github.com/dylanaraps/pure-sh-bible#get-the-base-name-of-a-file-path
basename() {
    dir=${1%${1##*[!/]}}
    dir=${dir##*/}
    dir=${dir%"$2"}
    base="${dir:-/}"
}

for p in pages/blog/*.md; do
    basename "$p"
    [ "$base" != "_index.md" ] &&
        cp "$p" "build/blog/${base%.*}.txt"
done
