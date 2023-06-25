"""Instructions

If you want to build something using a Raspberry Pi, you'll probably use resistors.
For this exercise, you need to know only three things about them:
Each resistor has a resistance value.
Resistors are small - so small in fact that if you printed the resistance value on them,
it would be hard to read. To get around this problem, manufacturers print color-coded
bands onto the resistors to denote their resistance values. Each band acts as a digit
of a number. For example, if they printed a brown band (value 1) followed by a green
band (value 5), it would translate to the number 15. In this exercise, you are going
to create a helpful program so that you don't have to remember the values of the bands.
The program will take 3 colors as input, and outputs the correct value, in ohms.
"""
import math

colors_scheme = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}


def convert_to_si_units(number):
    """setting prefix"""
    units = ["", "kilo", "mega", "giga"]
    index = 0
    while number >= 1000 and index < len(units) - 1:
        number /= 1000
        index += 1
    return f"{math.ceil(number)} {units[index]}"


def label(colors: list):
    """calculation resistance"""
    number = ""
    for color in colors[:2]:
        number += str(colors_scheme[color])
    ohms = colors_scheme[colors[2]] * "0"
    return f"{convert_to_si_units(int(number + ohms))}ohms"


print(label(["black", "grey", "black"]))
