#!/bin/sh

rm -rf go-vite
git clone https://github.com/icyphox/go-vite
cd go-vite && make && cd ..
mkdir build
go-vite/vite build
