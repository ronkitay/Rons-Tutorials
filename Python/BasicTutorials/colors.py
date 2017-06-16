#!/usr/bin/python
# -*- coding: utf-8 -*-

color_on_black_background = [
    ("\x1b[0;31;40m", "Red on Black background"),
    ("\x1b[0;32;40m", "Green on Black background"),
    ("\x1b[0;33;40m", "Yellow on Black background"),
    ("\x1b[0;34;40m", "Blue on Black background"),
    ("\x1b[0;35;40m", "Purple on Black background"),
    ("\x1b[0;36;40m", "Cyan on Black background"),
    ("\x1b[0;37;40m", "White on Black background")
]

bold_color_on_black_background = [
    ("\x1b[1;31;40m", "Bold Red on Black background"),
    ("\x1b[1;32;40m", "Bold Green on Black background"),
    ("\x1b[1;33;40m", "Bold Yellow on Black background"),
    ("\x1b[1;34;40m", "Bold Blue on Black background"),
    ("\x1b[1;35;40m", "Bold Purple on Black background"),
    ("\x1b[1;36;40m", "Bold Cyan on Black background"),
    ("\x1b[1;37;40m", "Bold White on Black background")
]

color_on_red_background = [
    ("\x1b[0;31;41m", "Red on Red background"),
    ("\x1b[0;32;41m", "Green on Red background"),
    ("\x1b[0;33;41m", "Yellow on Red background"),
    ("\x1b[0;34;41m", "Blue on Red background"),
    ("\x1b[0;35;41m", "Purple on Red background"),
    ("\x1b[0;36;41m", "Cyan on Red background"),
    ("\x1b[0;37;41m", "White on Red background")
]

bold_color_on_red_background = [
    ("\x1b[1;31;41m", "Bold Red on Red background"),
    ("\x1b[1;32;41m", "Bold Green on Red background"),
    ("\x1b[1;33;41m", "Bold Yellow on Red background"),
    ("\x1b[1;34;41m", "Bold Blue on Red background"),
    ("\x1b[1;35;41m", "Bold Purple on Red background"),
    ("\x1b[1;36;41m", "Bold Cyan on Red background"),
    ("\x1b[1;37;41m", "Bold White on Red background")
]

color_on_green_background = [
    ("\x1b[0;31;42m", "Red on Green background"),
    ("\x1b[0;32;42m", "Green on Green background"),
    ("\x1b[0;33;42m", "Yellow on Green background"),
    ("\x1b[0;34;42m", "Blue on Green background"),
    ("\x1b[0;35;42m", "Purple on Green background"),
    ("\x1b[0;36;42m", "Cyan on Green background"),
    ("\x1b[0;37;42m", "White on Green background")
]

bold_color_on_green_background = [
    ("\x1b[1;31;42m", "Bold Red on Green background"),
    ("\x1b[1;32;42m", "Bold Green on Green background"),
    ("\x1b[1;33;42m", "Bold Yellow on Green background"),
    ("\x1b[1;34;42m", "Bold Blue on Green background"),
    ("\x1b[1;35;42m", "Bold Purple on Green background"),
    ("\x1b[1;36;42m", "Bold Cyan on Green background"),
    ("\x1b[1;37;42m", "Bold White on Green background")
]

colors_to_print = [
    (color_on_black_background, bold_color_on_black_background),
    (color_on_red_background, bold_color_on_red_background),
    (color_on_green_background, bold_color_on_green_background)
]


def escape_color(color):
    return color.replace('\x1b', '\\x1b')


def print_colors(color_combination_1, color_combination_2):
    for a, b in zip(color_combination_1, color_combination_2):
        print ("{}{:<29}= {}\t\x1b[0m{}{:<35}= {}\x1b[0m".format(a[0], a[1], escape_color(a[0]), b[0], b[1],
                                                                 escape_color(b[0])))

for color_combination_1, color_combination_2 in colors_to_print:
    print_colors(color_combination_1, color_combination_2)

