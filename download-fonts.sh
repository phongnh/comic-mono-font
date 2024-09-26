#!/usr/bin/env sh

mkdir -p vendor

curl -SL https://github.com/shannpersand/comic-shanns/raw/refs/heads/master/v1/comic-shanns.otf -o vendor/comic-shanns.otf
curl -SL https://raw.githubusercontent.com/shannpersand/comic-shanns/master/v2/comic%20shanns.otf -o vendor/comic-shanns-v2.otf
curl -SL https://github.com/shannpersand/comic-shanns/raw/refs/heads/master/v2/comic%20shanns%202.ttf -o vendor/comic-shanns-v2.ttf
curl -SL https://raw.githubusercontent.com/google/fonts/main/apache/cousine/Cousine-Regular.ttf -o vendor/Cousine-Regular.ttf

