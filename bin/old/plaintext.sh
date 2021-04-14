#!/bin/sh

if ! command -v lynx
then
    printf '%s\n' "lynx not found, not going to run"
    exit
fi

for p in build/blog/**/index.html; do
    ppath="${p%%\/index.html}"
    pname="${ppath##build\/blog\/}"

    temp="$ppath/temp.html"
    # Not POSIX, I know
    sed -e '29,34d' "$p" > "$temp"
    cat "$temp" | awk -v OFS='\n\n' '/class="muted"/{n=3}; n {n--; next;} 1' > "$temp.new"
    mv "$temp.new" "$temp"

    txt="pages/txt/$pname.txt"
    lynx -dump "$temp" | tail -n +1 > "$txt"
    rm "$temp"
    sed -i 's/file:\/\/\//https:\/\/icyphox\.sh\//' "$txt"
done
