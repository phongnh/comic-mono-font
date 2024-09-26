#!/usr/bin/env sh

rm -f ./ComicMono*.ttf
fontforge ./generate.py vendor/comic-shanns.otf
fontforge ./generate-semibold.py vendor/comic-shanns.otf
[ -s vendor/IosevkaLarge-Regular.ttf ] && fontforge ./generate-large.py vendor/comic-shanns.otf
[ -s vendor/IosevkaLarge-Regular.ttf ] && fontforge ./generate-large-semibold.py vendor/comic-shanns.otf
./copy-fonts.sh
