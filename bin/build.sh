#!/bin/sh


rm -rf go-vite
git clone https://github.com/icyphox/go-vite
cd go-vite && make && cd ..
mkdir build

if [ "$VITE_ENV" = "production" ]; then
  go-vite/vite build
else
  go-vite/vite build --drafts
fi
