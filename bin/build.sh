#!/bin/sh


npm install tailwindcss @tailwindcss/cli

rm -rf go-vite
git clone https://tangled.sh/@icyphox.sh/vite
cd vite && make && cd ..
mkdir build

if [ "$VITE_ENV" = "production" ]; then
  vite/vite build
else
  vite/vite build --drafts
fi
