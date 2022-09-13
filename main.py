"""
Main.py
"""
from src.menu import menu_start, menu_file, menu_settings, menu_customize_settings, edit_sentence_newline, edit_comment_space, edit_emptylines, edit_enviroment_blocks_exclude, change_file_function
from src.file import File
from src.rules import Rules
from src.settings import Settings
from src.errors import WrongFile, WrongCommand

cleen_screen = chr(27) + "[2J" + chr(27) + "[;H"
green = '\x1b[1;32m'
blue = '\x1b[1;34m'
end_color = '\x1b[0m'

def main():
    """
    Main
    """
    ic = File() # File class
    rc = Rules() # Rules class
    sc = Settings() # Settings class
    while True:
        menu_start(sc.get_current_settings(), ic.get_current_file())

        choice = input(" Enter a action --> ")

        try:
            if choice == "1":
                """
                Change file
                """
                change_file_function(ic)

            elif choice == "2":
                """
                Edit rules
                """
                while True:
                    current_rule = sc.get_current_settings()
                    customized_settings = sc.get_settings("customized")
                    standard_settings = sc.get_settings("standard")
                    menu_settings(current_rule, standard_settings, customized_settings)
                    choiceRule = input(" Enter a action --> ")
                    try:
                        if choiceRule == "q":
                            break
                        elif choiceRule == "1":
                            """ Edit customize settings """
                            while True:
                                try:
                                    menu_customize_settings(customized_settings)

                                    change_setting = input(" Enter a action --> ")

                                    if change_setting == "1":
                                        """ Edit sentence-newline """
                                        edit_sentence_newline(sc)
                                        break

                                    elif change_setting == "2":
                                        """ Edit comment-space """
                                        edit_comment_space(sc)
                                        break

                                    elif change_setting == "3":
                                        """ Edit emptylines """
                                        edit_emptylines(sc)
                                        break

                                    elif change_setting == "4":
                                        """ Edit Enviroment blocks exclude """
                                        edit_enviroment_blocks_exclude(sc, customized_settings)
                                        break

                                    elif change_setting == "q":
                                        break

                                    raise WrongCommand

                                except WrongCommand:
                                    print("\nThat is not a valid choice.")
                                    input("\nPress enter to go back to Edit Customized settings menu...")

                        elif choiceRule == "2":
                            """ Change settings to use Customized settings """
                            sc.set_settings("customized")

                            print(green + "\nSettings has updated to use Customized Settings" + end_color)
                            input("\nPress enter to go back to main menu...")
                            break

                        elif choiceRule == "3":
                            """ Change settings to use Standard settings """
                            sc.set_settings("standard")

                            print(green + "\nSettings has updated to use Customized Settings" + end_color)
                            input("\nPress enter to go back to main menu...")
                            break

                        raise WrongCommand

                    except WrongCommand:
                        print("\nThat is not a valid choice.")
                        input("\nPress enter to go back to rule menu...")

            elif choice == "3":
                """
                Linter
                """
                break

            elif choice == "q":
                """ Exit the program """
                print("Thank you for using FalkenDev LaTeX Linter.")
                break

            raise WrongCommand

        except WrongCommand:
            print("\nThat is not a valid choice. Please choose from the menu.\n")
            input("Press enter to continue...")

if __name__ == "__main__":
    main()
