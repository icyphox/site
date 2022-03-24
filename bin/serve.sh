#!/bin/sh

vite serve &
find pages/ | entr vite build
