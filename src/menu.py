"""
menu.py
"""

import fnmatch
import os
from src.errors import WrongFile, WrongCommand, AlredyExists, DontExists, InstanceError

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

    print(purple + " Files to choose from input foler:\n" + end_color)
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
    print(" 4 ) Edit Enviroment blocks")
    print(" q ) Go Back")
    print(low_dash + "\n")


def change_file_function(ic):
    """
    Change file menu
    """
    while True:
        menu_file(ic.get_current_file())
        choice_file = input(" Enter a action --> ")
        try:
            if choice_file == "q":
                # Go back
                break

            if choice_file == "1":
                # Enters a specific file
                new_file = input(" Enter the file --> ")
                ic.set_file(new_file)
                print(green + "\n File has updated to use: " + new_file + end_color)
                input("\n Press enter to go back to main menu...")
                break

            raise WrongCommand # If wrong command has entered by user

        except WrongCommand:
            print("\n That is not a valid choice.")
            input("\n Press enter to go back to rule menu...")

        except WrongFile:
            print("\n You can't use that file, please try again.")
            input("\n Press enter to go back to rule menu...")

def edit_sentence_newline(settings):
    """ Edit sentence newline function """
    while True:
        print(blue + "\n Editing sentence-newline\n" + end_color)

        print(" 1 ) True")
        print(" 2 ) False\n")
        print(" q ) Go Back\n")

        custom_input = input(" Enter a action --> ")

        if custom_input == "1":
            print(settings.edit_custom_settings("sentence-newline", True))
            input("\n Press enter to go back to Settings Menu...")
            break

        if custom_input == "2":
            print(settings.edit_custom_settings("sentence-newline", False))
            input("\n Press enter to go back to Settings Menu...")
            break

        if custom_input == "q":
            break

        print(red + "\n That is not a valid choice." + end_color)

def edit_comment_space(settings):
    """ Edit comment space function """
    while True:
        menu_header("Editing comment-space", blue)
        print("\n Enter value of how much you want the comment-space to be")
        print("\n q ) Go back\n")

        custom_input = input(" Enter a value --> ")
        try:
            if custom_input.isnumeric():
                print(settings.edit_custom_settings("comment-space", int(custom_input)))
                input("\n Press enter to go back to Settings Menu...")
                break

            if custom_input == "q":
                break

            raise InstanceError

        except InstanceError:
            print(red + "\n That is not a valid choice." + end_color)

def edit_emptylines(settings):
    """ Edit emptylines function """
    while True:
        menu_header("Editing emptylines", blue)

        custom_input = input(" Enter a value --> ")
        try:
            if custom_input.isnumeric():
                print(settings.edit_custom_settings("emptylines", int(custom_input)))
                input("\n Press enter to go back to Edit Customized settings menu...")
                break

            if custom_input == "q":
                break

            raise InstanceError

        except InstanceError:
            print(red + "\n That is not a valid choice." + end_color)

def edit_enviroment_blocks_exclude(settings, customized_settings):
    """ Edit enviroment blocks exclude function """
    while True:
        menu_header("Edit Enviroment Blocks", blue)

        print(low_dash)
        print(" Enviroment blocks exclude list\n")
        for block in customized_settings["environment_blocks_exclude"]:
            print(" - " + block)
        print(low_dash)

        print(" Here you can choose if you want to exclude a enviroment block from /begin[itemize] or remove it from the exclude list\n")
        print(" 1 ) Add a new Enviroment block to exclude")
        print(" 2 ) Remove a Enviroment block from exclude list")
        print(" q ) Go Back\n")

        custom_input = input(" Enter a command --> ")

        try:
            if custom_input == "1":
                user_input = input("\n Enter a name you want to exclude --> ")
                print(settings.edit_enviroment_blocks_exclude_add(user_input))
                input("\n Press enter to go back to Edit Enviroment Blocks.")

            elif custom_input == "2":
                user_input = input("\n Enter a nem you want to remove from the exclude list --> ")
                print(settings.edit_enviroment_blocks_exclude_remove(user_input))
                input("\n Press enter to go back to Edit Enviroment Blocks.")

            elif custom_input == "q":
                break

            print(red + "\n That is not a valid choice." + end_color)

        except AlredyExists:
            print(red + "\n The name alredy exists in Enviroment blocks exclude list" + end_color)
            input("\n Press enter to go back to Edit Enviroment Blocks")

        except DontExists:
            print(red + "\n The name dosen't exists in Enviroment blocks exclude list" + end_color)
            input("\n Press enter to go back to Edit Enviroment Blocks")
