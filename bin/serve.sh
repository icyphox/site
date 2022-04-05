#!/usr/bin/env bash

kill_vite() {
    trap SIGINT
    echo "cleaning up..."
    pkill vite
    exit
}
trap "kill_vite" INT

vite serve &
find pages/ static/ templates/ | entr vite build

trap SIGINT
