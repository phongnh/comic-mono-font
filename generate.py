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

font = fontforge.open('vendor/comic-shanns.otf')
# ref = fontforge.open('vendor/Cousine-Regular.ttf')
# ref = fontforge.open('vendor/Inconsolata-Regular.ttf')
# ref = fontforge.open('vendor/iosevka-regular.ttf')
# ref = fontforge.open('vendor/iosevka-monaco-regular.ttf')
# ref = fontforge.open('vendor/iosevka-custom-regular.ttf')
ref = fontforge.open('vendor/iosevka-large-regular.ttf')
# ref = fontforge.open('vendor/mplus-1m-regular.ttf')
# ref = fontforge.open('vendor/FantasqueSansMono-ComicMono-Regular.ttf')
# ref = fontforge.open('vendor/mplus-1m-regular.ttf')
# ref = fontforge.open('vendor/FantasqueSansMono-Large-Regular.ttf')
# ref = fontforge.open('vendor/FantasqueSansMono-XtraLarge-Regular.ttf')

for g in font.glyphs():
    uni = g.unicode
    category = unicodedata.category(chr(uni)) if 0 <= uni <= sys.maxunicode else None
    if g.width > 0 and category not in ['Mn', 'Mc', 'Me']:
        target_width = 510
        # target_width = 510    # MPlus x 0.975
        # target_width = 515    # MPlus x 0.9375
        target_width = 520      # MPlus x 0.9375
        # target_width = 520    # MPlus x 0.95
        # target_width = 530    # Inconsolata x 1.025 (Same width as Shanns)
        # target_width = 520    # Inconsolata x 1.075
        target_width = 520      # Iosevka x 0.95
        # target_width = 510    # Iosevka Large x 0.975
        # target_width = 500    # Iosevka Large x 0.95
        # target_width = 510    # FantasqueSansMono x 1.025
        target_width = 520      # FantasqueSansMono x 1.025
        # target_width = 525    # FantasqueSansMono x 1.025
        # target_width = 530    # FantasqueSansMono x 0.975
        # target_width = 540    # FantasqueSansMono x 1.025
        # target_width = 540    # FantasqueSansMono x 1.050
        # target_width = 540    # FantasqueSansMono x 1.075
        if g.width != target_width:
            delta = target_width - g.width
            g.left_side_bearing = int(g.left_side_bearing + (delta / 2))
            g.right_side_bearing = int(g.right_side_bearing + delta - g.left_side_bearing)
            g.width = target_width

font.familyname = 'Comic Mono'
font.version = '0.1.1'
font.comment = 'https://github.com/dtinth/comic-mono-font'
font.copyright = 'https://github.com/dtinth/comic-mono-font/blob/master/LICENSE'

# adjust_height(font, ref, 0.825)
# adjust_height(font, ref, 0.925)   # MPlus x 520
# adjust_height(font, ref, 0.9375)  # MPlus x 520
# adjust_height(font, ref, 0.95)    # MPlus x 520
# adjust_height(font, ref, 0.975)   # MPlus x 510
# adjust_height(font, ref, 1.025)   # Inconsolata x 530 (Same width as Inconsolata)
# adjust_height(font, ref, 1.075)   # Inconsolata x 520
# adjust_height(font, ref, 0.95)    # Iosevka x 520 # GOOD
adjust_height(font, ref, 0.975)     # Iosevka x 520 # GOOD - BIGGER FONT
# adjust_height(font, ref, 1.025)   # Iosevka x 520
# adjust_height(font, ref, 0.96)    # Iosevka Large x 520
# adjust_height(font, ref, 0.90)    # Iosevka Large x 520
# adjust_height(font, ref, 0.95)    # Iosevka Large x 520
# adjust_height(font, ref, 0.975)   # Iosevka Large x 520
# adjust_height(font, ref, 0.99)    # Iosevka Large x 520 # Bigger! + 1475
# adjust_height(font, ref, 0.975)   # Iosevka Large x 510
# adjust_height(font, ref, 0.925)   # Iosevka Large x 520 (Same width as Iosevka)
# adjust_height(font, ref, 0.90)    # Iosevka Large x 500
# adjust_height(font, ref, 0.975)   # FantasqueSansMono x 530
# adjust_height(font, ref, 1.025)   # FantasqueSansMono x 510
# adjust_height(font, ref, 1.025)   # FantasqueSansMono x 520
# adjust_height(font, ref, 1.025)   # FantasqueSansMono x 525
# adjust_height(font, ref, 1.025)   # FantasqueSansMono x 540 # GOOD
# adjust_height(font, ref, 1.050)   # FantasqueSansMono x 540 # GOOD
# adjust_height(font, ref, 1.075)   # FantasqueSansMono x 540
# adjust_height(font, ref, 1.025)   # FantasqueSansMono (ComicMono) x 520 # GOOD
# adjust_height(font, ref, 1.050)   # FantasqueSansMono (ComicMono) x 520 # GOOD
# adjust_height(font, ref, 1.075)   # FantasqueSansMono (ComicMono) x 520 # GOOD
# adjust_height(font, ref, 1.100)   # FantasqueSansMono (ComicMono) x 520 # GOOD
# adjust_height(font, ref, 1.125)   # FantasqueSansMono (ComicMono) x 520 # GOOD # BIGGER FONT
# adjust_height(font, ref, 1.150)   # FantasqueSansMono (ComicMono) x 520 # GOOD # BIGGER FONT
font.sfnt_names = [] # Get rid of 'Prefered Name' etc.
font.fontname = 'ComicMono'
font.fullname = 'Comic Mono'
font.generate('ComicMono.ttf')

font.selection.all()
font.fontname = 'ComicMono-Bold'
font.fullname = 'Comic Mono Bold'
font.weight = 'Bold'
font.changeWeight(32, "LCG", 0, 0, "squish")
font.generate('ComicMono-Bold.ttf')
