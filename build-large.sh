#!/usr/bin/env sh

rm -f ./ComicMonoLarge.ttf ./ComicMonoLarge-Bold.ttf
fontforge ./generate-large.py
./copy-fonts.sh
