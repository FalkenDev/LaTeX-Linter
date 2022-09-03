"""
menu.py
"""

import fnmatch
import os

cleen_screen = chr(27) + "[2J" + chr(27) + "[;H"
low_dash = "_" * 40 + "\n"
headerslash = "/" * 56
green = '\x1b[1;32m'
blue = '\x1b[1;34m'
red = '\x1b[1;31m'
purple = '\x1b[1;35m'
end_color = '\x1b[0m'


def menustart():
    """Prints the start menu"""
    print(cleen_screen)

    print(green + headerslash + end_color)
    print("\n Welcome to FalkenDev LaTeX Linter\n")
    print(green + headerslash + end_color)

    print(low_dash)
    print(green + "Choosen File:" + end_color + " Undefined") # Edit the "Undefined" string to a function or a variable.
    print("")
    print(green + "Rules:" + end_color + " Standard") # Edit the "Standard" string to a function or a variable.
    print(low_dash)

    print('{:^40s}'.format(green + " Actions\n" + end_color))
    print(" 1 ) Change File")
    print(" 2 ) Edit rules")
    print(" 3 ) Start Lint the file / files")
    print(" q ) Exit / Close the program")
    print(low_dash + "\n")

def menufile():
    """Prints the Change File menu"""
    print(cleen_screen)

    print(purple + headerslash + end_color)
    print("\n Change File / Files\n")
    print(purple + headerslash + end_color)

    print(low_dash)
    print(purple + "Choosen File:" + end_color + " Undefined") # Edit the "Undefined" string to a function or a variable.
    print(low_dash)

    print(purple + "Files to choose from input foler:\n" + end_color)
    for file in os.listdir('./input'):
                if fnmatch.fnmatch(file, '*.tex'):
                    print(" - " + file)
                elif fnmatch.fnmatch(file, '*.bib'):
                    print(" - " + file)
                elif fnmatch.fnmatch(file, '*.tikz'):
                    print(" - " + file)
    print(low_dash)

    print('{:^40s}'.format(purple + " Actions\n" + end_color))
    print(" 1 ) All Files")
    print(" 2 ) Specific File")
    print(" q ) Go Back")
    print(low_dash + "\n")

def menurule(data):
    """Prints the Edit Rules menu"""
    print(cleen_screen)

    print(blue + headerslash + end_color)
    print("\n Edit Rules\n")
    print(blue + headerslash + end_color)

    print(low_dash)
    print(blue + "Rules:" + end_color + " Standard") # Edit the "standard" string to a function or a variable.
    print(low_dash)

    print(low_dash)
    print('{:^49s}'.format(green + " Standard Rules " + end_color))
    print('{:^53s}'.format(red + "( Unable to change Standard Rules ) \n" + end_color))
    for i in data["standard"]:
        print(blue + " " + i + ": "+ end_color + str(data["standard"][i]))
    print(low_dash)

    print(low_dash)
    print('{:^49s}'.format(green + " User Rules\n" + end_color))
    for i in data["user"]:
        print(blue + " " + i + ": "+ end_color + str(data["user"][i]))
    print(low_dash)

    print('{:^49s}'.format(blue + " Actions\n" + end_color))
    print(" 1 ) Edit User Rules")
    print(" 2 ) Change to Customized rules")
    print(" 3 ) Change to Standard rules")
    print(" q ) Go Back")
    print(low_dash + "\n")

