from discord import Colour
from host.units import INFANTRY, NAVY, AIRCRAFTS, LAND


COLOURS = {'teal': 0x1abc9c,
           'dark_teal': 0x11806a,
           'green': 0x2ecc71,
           'dark_green': 0x1f8b4c,
           'blue': 0x3498db,
           'dark_blue': 0x206694,
           'purple': 0x9b59b6,
           'dark_purple': 0x71368a,
           'magenta': 0xe91e63,
           'dark_magenta': 0xad1457,
           'gold': 0xf1c40f,
           'dark_gold': 0xc27c0e,
           'orange': 0xe67e22,
           'dark_orange': 0xa84300,
           'red': 0xe74c3c,
           'dark_red': 0x992d22,
           'lighter_grey': 0x95a5a6,
           'dark_grey': 0x607d8b,
           'light_grey': 0x979c9f,
           'darker_grey': 0x546e7a,
           'blurple': 0x7289da,
           'greyple': 0x99aab5}


def colour_vehicle(i):
    # 127.5,127.5,127.5 -> 0,255,255 -> 255,0,255
    if i < 3:
        r = int(100 + (42.5 * i))
        g = int(100 + (42.5 * i))
        b = int(100 + (42.5 * i))
    else:
        x = i - 2
        fac = 255 / 8
        r = int(255 - (fac * x))
        g = int(255)
        b = int(255 - (fac * x))
    return r, g, b


def colour_aircraft(i):
    # 127.5,127.5,127.5 -> 0,255,255 -> 255,0,255
    if i < 3:
        r = int(100 + (42.5 * i))
        g = int(100 + (42.5 * i))
        b = int(100 + (42.5 * i))
    else:
        x = i - 2
        fac = 115 / 8
        r = 140 + int(fac * x)
        g = 120 - int(fac * x)
        b = 140 + int(fac * x)
    return r, g, b


def colour_navy(i):
    # 127.5,127.5,127.5 -> 0,255,255 -> 255,0,255
    if i < 3:
        r = int(100 + (42.5 * i))
        g = int(100 + (42.5 * i))
        b = int(100 + (42.5 * i))
    else:
        x = i - 2
        fac = 115 / 7
        r = 120 - int(fac * x)
        g = 140 + int(fac * x)
        b = 140 + int(fac * x)
    return r, g, b


def colour_infantry(i):
    # 127.5,127.5,127.5 -> 0,255,255 -> 255,0,255
    if i < 3:
        r = int(100 + (42.5 * i))
        g = int(100 + (42.5 * i))
        b = int(100 + (42.5 * i))
    else:
        x = i - 2
        fac = 115 / 7
        r = 120 - int(fac * x)
        g = 140 + int(fac * x)
        b = 140 + int(fac * x)
    return r, g, b


UNIT_COLOURS = {INFANTRY: lambda i: colour_infantry(i),
                NAVY: lambda i: colour_navy(i),
                AIRCRAFTS: lambda i: colour_aircraft(i),
                LAND: lambda i: colour_vehicle(i)}


def get_colour(colour):
    """maps the name of the a colour to its value

    Args:
        colour (str): the name of the colour, or it's rgb components.

    Returns:
        int: hexadecimal value of the colour.
    """
    if colour.replace(' ', '_') in COLOURS.keys():
        return COLOURS[colour.replace(' ', '_')]
    else:
        colour = colour.split(',')
        colour = map(int, colour)
        Colour.from_rgb(*colour)
    return colour
