#!/usr/bin/env bash

export NO_CP=1
for img in static/img/*; do
    printf "uploading... $img: "
    u="$(~/bin/up $img)"
    printf "$u\n"
    new="![]("$u")"
    old="$img"
    printf "replacing $old with $new... "
    bin/replace "$old" "$new"
    printf "done\n"
done
