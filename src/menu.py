"""
menu.py
"""

import fnmatch
import os
from src.errors import WrongFile, WrongCommand, AlredyExists, DontExists

cleen_screen = chr(27) + "[2J" + chr(27) + "[;H"
LOW_DASH = "_" * 40 + "\n"
HEADER_SLASH = "/" * 56
GREEN = '\x1b[1;32m'
BLUE = '\x1b[1;34m'
RED = '\x1b[1;31m'
PURPLE = '\x1b[1;35m'
END_COLOR = '\x1b[0m'

# Shourtcuts ---------------------------------------------------------------------
def menu_header(header_title, color):
    "Prints menu header"
    print(cleen_screen)
    print(color + HEADER_SLASH + END_COLOR)
    print("\n " + header_title + "\n")
    print(color + HEADER_SLASH + END_COLOR)

def menu_file_info(color, current_file):
    "Prints current file info"
    print(LOW_DASH)
    print(color + " Choosen File: " + END_COLOR + current_file)
    print(LOW_DASH)

def menu_settings_info(color, current_settings):
    "Prints current settings"
    print(LOW_DASH)
    print(color + " Settings: " + END_COLOR + current_settings)
    print(LOW_DASH)

def menu_wrong_command():
    """ Prints wrong command exception"""
    print(" This is not a valid choise.")
    input(" Press enter to retry ")
#---------------------------------------------------------------------------------

# Menu Main ---------------------------------------------------------------------
def menu_start(current_settings, current_file):
    """Prints the start menu"""

    menu_header("Welcome to FalkenDev LaTeX Linter", GREEN)

    menu_file_info(GREEN, current_file)

    menu_settings_info(GREEN, current_settings)

    print('{:^40s}'.format(GREEN + " Actions\n" + END_COLOR))
    print(" 1 ) Change File")
    print(" 2 ) Settings")
    print(" 3 ) Start Lint the file / files")
    print(" q ) Exit / Close the program")
    print(LOW_DASH + "\n")
#---------------------------------------------------------------------------------

# Menu File ---------------------------------------------------------------------
def menu_file(current_file):
    """Prints the Change File menu"""

    menu_header("Change File / Files", PURPLE)

    menu_file_info(PURPLE, current_file)

    print(PURPLE + " Files to choose from input foler:\n" + END_COLOR)
    for file in os.listdir('./input'):
        if fnmatch.fnmatch(file, '*.tex'):
            print(" - " + file)
    print(LOW_DASH)

    print('{:^40s}'.format(PURPLE + " Actions\n" + END_COLOR))
    print(" 1 ) Specific File")
    print(" q ) Go Back")
    print(LOW_DASH + "\n")

def change_file_function(file_class):
    """
    Change file menu
    """
    while True:
        menu_file(file_class.get_current_file())
        choice_file = input(" Enter a action --> ")
        try:
            if choice_file == "q":
                # Go back
                break

            if choice_file == "1":
                # Enters a specific file
                new_file = input("\n Enter the file name --> ")
                file_class.set_file(new_file)
                print(GREEN + "\n File has updated to use: " + new_file + END_COLOR)
                input("\n Press enter to go back to main menu...")
                break

            else:
                raise WrongCommand # If wrong command has entered by user

        except WrongCommand:
            print("\n That is not a valid choices")
            input("\n Press enter to go back to rule menu...")

        except WrongFile:
            print("\n You can't use that file, please try again.")
            input("\n Press enter to go back to rule menu...")
#---------------------------------------------------------------------------------

# Menu Settings ---------------------------------------------------------------------
def menu_settings(current_settings, standard_settings, customized_settings):
    """Prints the Edit Settings menu"""

    menu_header("Settings", BLUE)

    menu_settings_info(BLUE, current_settings)

    print(LOW_DASH)
    print('{:^49s}'.format(GREEN + " Standard Settings " + END_COLOR))
    print('{:^53s}'.format(RED + "( Unable to change Standard Settings ) \n" + END_COLOR))
    for i in standard_settings:
        print(BLUE + " " + i + ": "+ END_COLOR + str(standard_settings[i]))
    print(LOW_DASH)

    print(LOW_DASH)
    print('{:^49s}'.format(GREEN + " Customized Settings\n" + END_COLOR))
    for i in customized_settings:
        print(BLUE + " " + i + ": "+ END_COLOR + str(customized_settings[i]))
    print(LOW_DASH)

    print('{:^49s}'.format(BLUE + " Actions\n" + END_COLOR))
    print(" 1 ) Edit Customized settings")
    print(" 2 ) Change to Customized settings")
    print(" 3 ) Change to Standard settings")
    print(" q ) Go Back")
    print(LOW_DASH + "\n")
#---------------------------------------------------------------------------------

# Menu Customize Settings ---------------------------------------------------------------------
def menu_customize_settings(customized_settings):
    """ Prints the cusomized settings and gives options what to change """

    menu_header("Edit Customized settings", BLUE)

    print(LOW_DASH)
    print('{:^49s}'.format(GREEN + " Customized Settings\n" + END_COLOR))
    for i in customized_settings:
        print(BLUE + " " + i + ": "+ END_COLOR + str(customized_settings[i]))
    print(LOW_DASH)

    print('{:^49s}'.format(BLUE + " Actions\n" + END_COLOR))
    print(" 1 ) Edit sentence-newline")
    print(" 2 ) Edit comment-space")
    print(" 3 ) Edit emptylines")
    print(" 4 ) Edit Enviroment blocks")
    print(" q ) Go Back")
    print(LOW_DASH + "\n")

def edit_sentence_newline(settings):
    """ Edit sentence newline function """
    while True:
        menu_header("Editing sentence-newline", BLUE)
        print("\n ● Newline after a sentence for better git support ")

        print("\n Here you can choose if u want to set sentence-newline rule to true or false\n")

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

        menu_wrong_command()

def edit_comment_space(settings):
    """ Edit comment space function """
    while True:
        menu_header("Editing comment-space", BLUE)
        print("\n Enter value of how much you want the comment-space to be")
        print("\n q ) Go back\n")

        custom_input = input(" Enter a value --> ")
        if custom_input.isnumeric():
            print(settings.edit_custom_settings("comment-space", int(custom_input)))
            input("\n Press enter to go back to Settings Menu...")
            break

        if custom_input == "q":
            break

        menu_wrong_command()

def edit_emptylines(settings):
    """ Edit emptylines function """
    while True:
        menu_header("Editing emptylines", BLUE)

        print("\n ● Blank lines before section, chapter, etc.")
        print("\n Enter a value of how many blank lines you want to have.\n")
        print("\n q ) Go back\n")

        custom_input = input(" Enter a value --> ")
        if custom_input.isnumeric():
            print(settings.edit_custom_settings("emptylines", int(custom_input)))
            input("\n Press enter to go back to Edit Customized settings menu...")
            break

        if custom_input == "q":
            break

        menu_wrong_command()

def edit_enviroment_blocks_exclude(settings, customized_settings):
    """ Edit enviroment blocks exclude function """
    while True:
        menu_header("Edit Enviroment Blocks", BLUE)

        print(LOW_DASH)
        print(" Enviroment blocks exclude list\n")
        for block in customized_settings["environment_blocks_exclude"]:
            print(" - " + block)
        print(LOW_DASH)

        print(
            " Here you can choose if you want to exclude a"
            " enviroment block from example /part[itemize] or remove it from the exclude list\n"
        )
        print(" 1 ) Add a new Enviroment block to exclude")
        print(" 2 ) Remove a Enviroment block from exclude list")
        print(" q ) Go Back\n")

        custom_input = input(" Enter a command --> ")

        try:
            if custom_input == "1":
                user_input = input("\n Enter a name you want to exclude --> ")
                print(settings.edit_enviroment_blocks_exclude_add(user_input))
                input("\n Press enter to go back to Edit Enviroment Blocks.")
                customized_settings = settings.get_settings("customized")

            elif custom_input == "2":
                user_input = input("\n Enter a nem you want to remove from the exclude list --> ")
                print(settings.edit_enviroment_blocks_exclude_remove(user_input))
                input("\n Press enter to go back to Edit Enviroment Blocks.")
                customized_settings = settings.get_settings("customized")

            elif custom_input == "q":
                break

            else:
                menu_wrong_command()

        except AlredyExists:
            print(RED + "\n The name alredy exists in Enviroment blocks exclude list" + END_COLOR)
            input("\n Press enter to go back to Edit Enviroment Blocks")

        except DontExists:
            print(RED + "\n The name dosen't exists in Enviroment blocks exclude list" + END_COLOR)
            input("\n Press enter to go back to Edit Enviroment Blocks")
#---------------------------------------------------------------------------------
