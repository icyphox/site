#!/usr/bin/env bash
#
# usage: printf "<bunch of photos>" | ./bin/photos.sh >> pages/photos.md

prefix="$1"
printf '<div class="image-grid">\n'
while IFS=$'\n' read -r line; do
    printf '  <a href="https://cdn.icyphox.sh/film/%s">\n' "$prefix/$line"
    printf '    <img src="https://cdn.icyphox.sh/fit?file=%s&width=1000&height=1000" />\n' "$prefix/$line"
    printf '  </a>\n'
done < /dev/stdin
printf '</div>'
