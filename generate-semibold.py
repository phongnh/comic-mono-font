#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Generates the Comic Mono font files based on Comic Shanns font.

Required files:
- vendor/comic-shanns.otf
- vendor/Cousine-Regular.ttf

Based on:
- monospacifier: https://github.com/cpitclaudel/monospacifier/blob/master/monospacifier.py
- YosemiteAndElCapitanSystemFontPatcher: https://github.com/dtinth/YosemiteAndElCapitanSystemFontPatcher/blob/master/bin/patch
"""

import os
import re
import sys
from importlib import reload

reload(sys)

import fontforge
import psMat
import unicodedata

def height(font):
    return float(font.capHeight)

def adjust_height(source, template, scale):
    source.selection.all()
    height_scale = height(template) / height(source)
    print()
    print(f'height(template) = {height(template)}')
    print(f'height(source) = {height(source)}')
    print(f'height_scale = {height_scale}')
    print(f'scale = {scale}')
    print()
    source.transform(psMat.scale(height(template) / height(source)))
    for attr in ['ascent', 'descent',
                'hhea_ascent', 'hhea_ascent_add',
                'hhea_linegap',
                'hhea_descent', 'hhea_descent_add',
                'os2_winascent', 'os2_winascent_add',
                'os2_windescent', 'os2_windescent_add',
                'os2_typoascent', 'os2_typoascent_add',
                'os2_typodescent', 'os2_typodescent_add',
                ]:
        setattr(source, attr, getattr(template, attr))
    # adjust_line_height(source)
    source.transform(psMat.scale(scale))

def adjust_line_height(source):
    if (source.os2_winascent + source.os2_windescent) % 2 != 0:
        source.os2_winascent += 1
    # Make the line size identical for windows and mac
    source.hhea_ascent = source.os2_winascent
    source.hhea_descent = -source.os2_windescent
    # Line gap add extra space on the bottom of the line which
    # doesn't allow the powerline glyphs to fill the entire line.
    source.hhea_linegap = 0
    source.os2_typolinegap = 0

source_font = len(sys.argv) > 1 and sys.argv[1] or 'vendor/comic-shanns.otf'
print()
print(f'Source font: {source_font}')
print()

font = fontforge.open(source_font)
# font = fontforge.open('vendor/comic-shanns.otf')
# ref = fontforge.open('vendor/Cousine-Regular.ttf')
ref = fontforge.open('vendor/Iosevka-Regular.ttf')

for g in font.glyphs():
    uni = g.unicode
    category = unicodedata.category(chr(uni)) if 0 <= uni <= sys.maxunicode else None
    if g.width > 0 and category not in ['Mn', 'Mc', 'Me']:
        target_width = 520      # Iosevka x 0.95
        if g.width != target_width:
            delta = target_width - g.width
            g.left_side_bearing = int(g.left_side_bearing + (delta / 2))
            g.right_side_bearing = int(g.right_side_bearing + delta - g.left_side_bearing)
            g.width = target_width

font.familyname = 'Comic Mono'
font.version = '1.0.0'
font.comment = 'https://github.com/dtinth/comic-mono-font'
font.copyright = 'https://github.com/dtinth/comic-mono-font/blob/master/LICENSE'

# adjust_height(font, ref, 0.825)
# adjust_height(font, ref, 0.95)    # Iosevka x 520 # GOOD
adjust_height(font, ref, 0.975)     # Iosevka x 520 # GOOD - BIGGER FONT
# adjust_height(font, ref, 0.99)    # Iosevka Large x 520 # Bigger! + 1475
# adjust_height(font, ref, 0.925)   # Iosevka Large x 520 (Same width as Iosevka)
font.sfnt_names = [] # Get rid of 'Prefered Name' etc.

font.selection.all()
font.fontname = 'ComicMono-SemiBold'
font.fullname = 'Comic Mono SemiBold'
font.weight = 'SemiBold'
font.changeWeight(16, "LCG", 0, 0, "squish")
font.weight = 'semibold'
font.generate('ComicMono-SemiBold.ttf')
