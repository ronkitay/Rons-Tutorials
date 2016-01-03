#!/usr/bin/python
# -*- coding: utf-8 -*-

# Prints the following:
# \u0x05D0 = א      \u0x05D1 = ב    \u0x05D2 = ג    \u0x05D3 = ד    \u0x05D4 = ה
# \u0x05D5 = ו      \u0x05D6 = ז    \u0x05D7 = ח     \u0x05D8 = ט   \u0x05D9 = י
# \u0x05DA = ך      \u0x05DB = כ    \u0x05DC = ל    \u0x05DD = ם    \u0x05DE = מ
# \u0x05DF = ן      \u0x05E0 = נ    \u0x05E1 = ס    \u0x05E2 = ע    \u0x05E3 = ף
# \u0x05E4 = פ      \u0x05E5 = ץ    \u0x05E6 = צ    \u0x05E7 = ק    \u0x05E8 = ר
# \u0x05E9 = ש      \u0x05EA = ת
# \u0x05B0 = ְ    \u0x05B1 = ֱ    \u0x05B2 = ֲ    \u0x05B3 = ֳ    \u0x05B4 = ִ
# \u0x05B5 = ֵ    \u0x05B6 = ֶ    \u0x05B7 = ַ    \u0x05B8 = ָ    \u0x05B9 = ֹ

for index in range(0,27):
    base = 0x05d0
    character = base + index
    print '\\u0x%0.4X = %s' % (character, unichr(character).encode('utf-8'))

for index in range(0,10):
    base = 0x05b0
    character = base + index
    print '\\u0x%0.4X = %s' % (character, unichr(character).encode('utf-8'))
