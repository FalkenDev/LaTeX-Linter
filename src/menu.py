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

def menu_header(header_title, color):
    "Prints menu header"
    print(cleen_screen)
    print(color + headerslash + end_color)
    print("\n " + header_title + "\n")
    print(color + headerslash + end_color)

def menu_file_info(color, current_file):
    "Prints current file info"
    print(low_dash)
    print(color + " Choosen File: " + end_color + current_file)
    print(low_dash)

def menu_settings_info(color, current_settings):
    "Prints current settings"
    print(low_dash)
    print(color + " Settings: " + end_color + current_settings)
    print(low_dash)


def menu_start(current_settings, current_file):
    """Prints the start menu"""

    menu_header("Welcome to FalkenDev LaTeX Linter", green)

    menu_file_info(green, current_file)

    menu_settings_info(green, current_settings)

    print('{:^40s}'.format(green + " Actions\n" + end_color))
    print(" 1 ) Change File")
    print(" 2 ) Settings")
    print(" 3 ) Start Lint the file / files")
    print(" q ) Exit / Close the program")
    print(low_dash + "\n")

def menu_file(current_file):
    """Prints the Change File menu"""

    menu_header("Change File / Files", purple)

    menu_file_info(purple, current_file)

    print(purple + "Files to choose from input foler:\n" + end_color)
    for file in os.listdir('./input'):
        if fnmatch.fnmatch(file, '*.tex'):
            print(" - " + file)
    print(low_dash)

    print('{:^40s}'.format(purple + " Actions\n" + end_color))
    print(" 1 ) Specific File")
    print(" q ) Go Back")
    print(low_dash + "\n")

def menu_settings(current_settings, standard_settings, customized_settings):
    """Prints the Edit Settings menu"""

    menu_header("Settings", blue)

    menu_settings_info(blue, current_settings)

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

    menu_header("Edit Customized settings", blue)

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
