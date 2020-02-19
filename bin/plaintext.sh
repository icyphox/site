#!/bin/sh 

# from the pure sh bible; see: 
# https://github.com/dylanaraps/pure-sh-bible#get-the-base-name-of-a-file-path
basename() {
    dir=${1%${1##*[!/]}}
    dir=${dir##*/}
    dir=${dir%"$2"}
    base="${dir:-/}"
}

# prepare the '_redirects' file
printf 'http://icyphox.netlify.com/* http://icyphox.sh/:splat 301!\n' > build/_redirects
for p in pages/blog/*.md; do
    basename "$p"
    no_ext="${base%.*}"
    [ "$base" != "_index.md" ] && {
        pandoc --quiet -s -f "markdown+gutenberg" \
            "$p" -o "pages/txt/$no_ext.txt"
            printf '%s\n' "/txt/$no_ext.txt /txt/$no_ext 301" >> build/_redirects
    }
done

