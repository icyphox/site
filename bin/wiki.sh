#!/usr/bin/env bash

# wiki.sh -- helper script to generate a wiki
# does all kinds of weird shit. this is NOT how you engineer software, people.

WIKI_PATH="pages/wiki"
ROOT_INDEX_MD="pages/wiki/_index.md"

generate_index() {
    mapfile -d $'\0' entries < <(find "$WIKI_PATH" ! -path "$WIKI_PATH" -print0)
    prevdir=''
    for r in "${entries[@]}"; do
        path="$(basename "$r")"
        [ "$path" != "_index.md" ] && {
            if [ -d "$r" ]; then
                printf '%s\n' "- [$path](/wiki/$path)"
                prevdir="$path"
            elif [ "$(basename "$(dirname "$r")")" == "$prevdir" ]; then
                noext="${path%%'.md'}"
                printf '  %s\n' "- [$noext](/wiki/$prevdir/$noext)"
            else
                printf '%s\n' "- [$path](/wiki/$path)"
            fi
        }
    done
}

printf '%s' "---
title: wiki
subtitle: Ideas, beliefs and thoughts.
template: page.html
---

# The wiki.

" > "$ROOT_INDEX_MD"
generate_index >> "$ROOT_INDEX_MD"

exit 0
