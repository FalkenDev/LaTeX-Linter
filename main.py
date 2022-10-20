"""
Main.py
"""
# pylint: disable=too-many-branches
# pylint: disable=too-many-statements
# pylint: disable=too-many-nested-blocks
import time
from src.menu import (menu_start, menu_settings, menu_customize_settings,
edit_sentence_newline, edit_comment_space, edit_emptylines,
edit_enviroment_blocks_exclude, change_file_function)
from src.file import File
from src.rules import Rules
from src.settings import Settings
from src.errors import WrongCommand, ErrorDataLoaded

cleen_screen = chr(27) + "[2J" + chr(27) + "[;H"
GREEN = '\x1b[1;32m'
BLUE = '\x1b[1;34m'
END_COLOR = '\x1b[0m'

def main():
    """
    Main
    """
    file_class = File() # File class
    settings_class = Settings() # Settings class

    while True:
        menu_start(settings_class.get_current_settings(), file_class.get_current_file())

        choice = input(" Enter a action --> ")

        try:
            if choice == "1":
                # Change file """
                change_file_function(file_class)


            elif choice == "2":
                # Edit rules
                while True:
                    current_rule = settings_class.get_current_settings()
                    customized_settings = settings_class.get_settings("customized")
                    standard_settings = settings_class.get_settings("standard")
                    menu_settings(current_rule, standard_settings, customized_settings)
                    choice_rule = input(" Enter a action --> ")
                    try:
                        if choice_rule == "q":
                            break
                        if choice_rule == "1":
                            # Edit customize settings
                            while True:
                                try:
                                    menu_customize_settings(customized_settings)

                                    change_setting = input(" Enter a action --> ")

                                    if change_setting == "1":
                                        # Edit sentence-newline
                                        edit_sentence_newline(settings_class)
                                        break

                                    elif change_setting == "2":
                                        # Edit comment-space
                                        edit_comment_space(settings_class)
                                        break

                                    elif change_setting == "3":
                                        # Edit emptylines
                                        edit_emptylines(settings_class)
                                        break

                                    elif change_setting == "4":
                                        # Edit Enviroment blocks exclude
                                        edit_enviroment_blocks_exclude(
                                            settings_class,
                                            customized_settings
                                        )
                                        break

                                    elif change_setting == "q":
                                        break

                                    raise WrongCommand

                                except WrongCommand:
                                    print("\n That is not a valid choice.")
                                    input(
                                        "\n Press enter to go back to"
                                        " Edit Customized settings menu..."
                                    )

                        elif choice_rule == "2":
                            # Change settings to use Customized settings
                            settings_class.set_settings("customized")

                            print(
                                GREEN + "\n Settings has updated"
                                " to use Customized Settings" + END_COLOR
                            )
                            input("\n Press enter to go back to main menu...")
                            break

                        elif choice_rule == "3":
                            # Change settings to use Standard settings
                            settings_class.set_settings("standard")

                            print(
                                GREEN + "\n Settings has updated"
                                " to use Standard Settings" + END_COLOR
                            )
                            input("\n Press enter to go back to main menu...")
                            break

                    except WrongCommand:
                        print("\n That is not a valid choice.")
                        input("\n Press enter to go back to rule menu...")

            elif choice == "3":
                try:
                    start_time = time.time()
                    file_path = file_class.get_current_filename()
                    filename = file_class.get_current_file()
                    settings_json_data = settings_class.get_settings(
                        settings_class.get_current_settings()
                    )
                    Rules(filename, file_path, settings_json_data)
                    print(
                        GREEN + "\n Took: " +
                        str(time.time() - start_time)[:6] +
                        " seconds to Lint the TeX file" + END_COLOR
                    )
                    print(
                        GREEN + "\nThe file: " + filename +
                        " has been validated and linted with settings: " +
                        settings_class.get_current_settings() + END_COLOR
                    )
                    input("\n Press enter to go back to main menu...")
                except ErrorDataLoaded:
                    print("\n The file and settings have not been loaded correctly!")
                    input("\n Press enter to go back to rule menu...")

            elif choice == "q":
                # Exit the program
                print(" Thank you for using FalkenDev LaTeX Linter.")
                break

            else:
                raise WrongCommand

        except WrongCommand:
            print("\n That is not a valid choice. Please choose from the menu.\n")
            input(" Press enter to continue...")

if __name__ == "__main__":
    main()
