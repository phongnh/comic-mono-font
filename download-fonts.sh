#!/usr/bin/env sh

mkdir -p vendor

curl -SL https://raw.githubusercontent.com/shannpersand/comic-shanns/master/v2/comic%20shanns.otf -o vendor/comic-shanns.otf

curl -SL https://raw.githubusercontent.com/google/fonts/main/apache/cousine/Cousine-Regular.ttf -o vendor/Cousine-Regular.ttf

