#!/usr/bin/env sh

rm -f ./ComicMono*.ttf
fontforge ./generate.py vendor/comic-shanns-v2.otf
fontforge ./generate-semibold.py vendor/comic-shanns-v2.otf
[ -s vendor/IosevkaLarge-Regular.ttf ] && fontforge ./generate-large.py vendor/comic-shanns-v2.otf
[ -s vendor/IosevkaLarge-Regular.ttf ] && fontforge ./generate-large-semibold.py vendor/comic-shanns-v2.otf
./copy-fonts.sh
