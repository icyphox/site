#!/usr/bin/env bash

# wiki.sh -- helper script to generate a wiki
# does all kinds of weird shit. this is NOT how you engineer software, people.

WIKI_PATH="pages/wiki"
ROOT_INDEX_MD="pages/wiki/_index.md"

noext() {
   printf '%s' "${1%%'.md'}"
}

topic() {
    entry="$1"
    mkdir "$WIKI_PATH/$entry"
    printf '%s' "---
title: $entry
subtitle:
date: $(date +'%Y-%m-%d')
template: page.html
---" > "$WIKI_PATH/$entry/"_index.md

}

generate_index() {
    mapfile -t entries < <(find "$WIKI_PATH" ! -path "$WIKI_PATH" | sort)
    prevdir=''
    for r in "${entries[@]}"; do
        path="$(basename "$r")"
        [ "$path" != "_index.md" ] && {
            if [ -d "$r" ]; then
                printf '%s\n' "- [$path](/wiki/$path)"
                prevdir="$path"
            elif [ "$(basename "$(dirname "$r")")" == "$prevdir" ]; then
                noext="$(noext "$path")"
                printf '  %s\n' "- [$noext](/wiki/$prevdir/$noext)"
            else
                noext="$(noext "$path")"
                printf '%s\n' "- [$noext](/wiki/$noext)"
            fi
        }
    done
    exit 0
}

link() {
    # FIXME: this needs to be reworked
    # post A, and post B
    a="$(noext "$1")"
    a="${a#"$WIKI_PATH"}"
    b="$(noext "$2")"
    b="${a#"$WIKI_PATH"}"

    printf '%s' "- [$a](/wiki/$a)" >> "$2"
    printf '%s' "- [$b](/wiki/$b)" >> "$1"
}

if [ "$#" -eq 0 ]; then
    printf '%s' "---
title: the wiki
subtitle: A collection of notes on various topics.
date: $(date +'%Y-%m-%d')
template: page.html
---

" > "$ROOT_INDEX_MD"
    generate_index >> "$ROOT_INDEX_MD"
else
    case "$1" in
        "topic")
            shift
            topic "$1"
            ;;
    esac
fi
