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


def menu_start(current_settings, current_file):
    """Prints the start menu"""
    print(cleen_screen)

    print(green + headerslash + end_color)
    print("\n Welcome to FalkenDev LaTeX Linter\n")
    print(green + headerslash + end_color)

    print(low_dash)
    print(green + " Choosen File: " + end_color + current_file) # Edit the "Undefined" string to a function or a variable.
    print("")
    print(green + " Settings: " + end_color + current_settings) # Edit the "Standard" string to a function or a variable.
    print(low_dash)

    print('{:^40s}'.format(green + " Actions\n" + end_color))
    print(" 1 ) Change File")
    print(" 2 ) Settings")
    print(" 3 ) Start Lint the file / files")
    print(" q ) Exit / Close the program")
    print(low_dash + "\n")

def menu_file(current_file):
    """Prints the Change File menu"""
    print(cleen_screen)

    print(purple + headerslash + end_color)
    print("\n Change File / Files\n")
    print(purple + headerslash + end_color)

    print(low_dash)
    print(purple + "Choosen File: " + end_color + current_file) # Edit the "Undefined" string to a function or a variable.
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

def menu_settings(current_settings, standard_settings, customized_settings):
    """Prints the Edit Settings menu"""
    print(cleen_screen)

    print(blue + headerslash + end_color)
    print("\n Settings\n")
    print(blue + headerslash + end_color)

    print(low_dash)
    print(blue + "Settings: " + end_color + current_settings) # Edit the "standard" string to a function or a variable.
    print(low_dash)

    print(low_dash)
    print('{:^49s}'.format(green + " Standard Settings " + end_color))
    print('{:^53s}'.format(red + "( Unable to change Standard Settings ) \n" + end_color))
    for i in standard_settings:
        print(blue + " " + i + ": "+ end_color + str(standard_settings[i]))
    print(low_dash)

    print(low_dash)
    print('{:^49s}'.format(green + " Customized Settings\n" + end_color))
    for i in customized_settings:
        print(blue + " " + i + ": "+ end_color + str(customized_settings[i]))
    print(low_dash)

    print('{:^49s}'.format(blue + " Actions\n" + end_color))
    print(" 1 ) Edit Customized settings")
    print(" 2 ) Change to Customized settings")
    print(" 3 ) Change to Standard settings")
    print(" q ) Go Back")
    print(low_dash + "\n")

def menu_customize_settings(customized_settings):
    """ Prints the cusomized settings and gives options what to change """
    print(cleen_screen)

    print(blue + headerslash + end_color)
    print("\n Edit Customized settings\n")
    print(blue + headerslash + end_color)

    print(low_dash)
    print('{:^49s}'.format(green + " Customized Settings\n" + end_color))
    for i in customized_settings:
        print(blue + " " + i + ": "+ end_color + str(customized_settings[i]))
    print(low_dash)

    print('{:^49s}'.format(blue + " Actions\n" + end_color))
    print(" 1 ) Edit sentence-newline")
    print(" 2 ) Edit comment-space")
    print(" 3 ) Edit emptylines")
    print(" q ) Go Back")
    print(low_dash + "\n")
