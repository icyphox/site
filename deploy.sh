#!/usr/bin/env bash

if [ -z "$1" ]
then
	echo "no folder mentioned :v"
	exit 1
fi
git subtree push --prefix $1 origin gh-pages
