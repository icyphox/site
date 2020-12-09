#!/bin/sh

rm -rf go-vite
git clone https://github.com/icyphox/go-vite
cd go-vite && make && cd ..
mkdir -p build/txt
go-vite/vite build
cp -r pages/txt/* build/txt
