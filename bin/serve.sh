#!/usr/bin/env bash

vite="$1"
if [ -z "$vite" ]; then
    vite="vite"
fi

echo "using vite command: $vite"

kill_vite() {
    trap SIGINT
    echo "cleaning up..."
    pkill vite
    exit
}
trap "kill_vite" INT

"$vite" serve &
find pages/ static/ templates/ | entr "$vite" build --drafts

trap SIGINT
