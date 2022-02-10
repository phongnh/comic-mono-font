#!/usr/bin/env sh

rm -f ./ComicMono.ttf ./ComicMono-Bold.ttf
fontforge ./generate.py
./copy-fonts.sh
