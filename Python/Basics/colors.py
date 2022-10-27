from random import choice
from termcolor import *

text = "Who were you before people started telling you who you should be?"
cprint(text, "cyan")


def print_in_random_color(text):
    colors = ("red", "green", "blue", "magenta")
    return cprint(text, choice(colors), end="")


print_in_random_color("Hello World!\n")

image = \
    """
                .,aadd"'    `"bbaa,.
            ,ad8888P'          `Y8888ba,
         ,a88888888              88888888a,
       a88888888888              88888888888a
     a8888888888888b,          ,d8888888888888a
    d8888888888888888b,_    _,d8888888888888888b
   d88888888888888888888888888888888888888888888b
  d8888888888888888888888888888888888888888888888b
 I888888888888888888888888888888888888888888888888I
,88888888888888888888888888888888888888888888888888,
I8888888888888888PY8888888PY88888888888888888888888I
8888888888888888"  "88888"  "88888888888888888888888
8::::::::::::::'    `:::'    `:::::::::::::::::::::8
Ib:::::::::::"        "        `::::::' `:::::::::dI
`8888888888P            Y88888888888P     Y88888888'
 Ib:::::::'              `:::::::::'       `:::::dI
  Yb::::"                  ":::::"           "::dP
   Y88P                      Y8P               `P
    Y'                        "
                                `:::::::::::;8"
       "888888888888888888888888888888888888"
         `"8;::::::::::::::::::::::::::;8"'
            `"Ya;::::::::::::::::::;aP"'
                ``""YYbbaaaaddPP""''"""


for char in image:
    if char == '\n':
        print()
    else:
        print_in_random_color(char)
