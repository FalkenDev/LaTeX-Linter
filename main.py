"""
Main.py
"""
from src.menu import menu_start, menu_file, menu_settings, menu_customize_settings
from src.input import Input
from src.rules import Rules
from src.settings import Settings

cleen_screen = chr(27) + "[2J" + chr(27) + "[;H"
green = '\x1b[1;32m'
blue = '\x1b[1;34m'
end_color = '\x1b[0m'

def main():
    """
    Main
    """
    ic = Input() # Input class
    rc = Rules() # Rules class
    sc = Settings() # Settings class
    while True:
        menu_start(sc.get_current_settings(), ic.get_current_file())

        choice = input(" Enter a action --> ")

        if choice == "1":
            """
            Change file
            """
            while True:
                menu_file(ic.get_current_file())
                choiceFile = input(" Enter a action --> ")
                try:
                    if choiceFile == "q":
                        break
                    elif choiceFile == "1":
                        break # Maybe implement this | Sooner
                    elif choiceFile == "2":
                        new_file = input("Enter the file --> ")
                        ic.set_file(new_file)
                        if new_file == ic.get_current_file(): # Change this soon after fixed customized exception when the file is not working
                            print(green + "\nFile has updated to use: " + new_file + end_color)
                            input("\nPress enter to go back to main menu...")
                            break
                        print("Ops, you have entered wrong file name from the list!")
                        input("\nPress enter to go back to rule menu...")
                        

                    else:
                        raise KeyError
                except KeyError:
                    print("\nThat is not a valid choice.")
                    input("\nPress enter to go back to rule menu...")

        elif choice == "2":
            """
            Edit rules
            """
            while True:
                current_rule = sc.get_current_settings()
                customized_settings = sc.get_custom_settings()
                standard_settings = sc.get_standard_settings()
                menu_settings(current_rule, standard_settings, customized_settings)
                choiceRule = input(" Enter a action --> ")
                try:
                    if choiceRule == "q":
                        break
                    elif choiceRule == "1":
                        while True:
                            menu_customize_settings(customized_settings)
                            change_setting = input(" Enter a action --> ")
                            if change_setting == "1":
                                while True:
                                    print(blue + "\nEditing sentence-newline\n" + end_color)
                                    print(" 1 ) True")
                                    print(" 2 ) False\n")
                                    custom_input = input(" Enter a action --> ")
                                    if custom_input == "1":
                                        sc.edit_custom_settings("sentence-newline", True)
                                        print(green + "\nSetting sentence-newline has updated to: True" + end_color)
                                        input("\nPress enter to go back to Edit Customized settings menu...")
                                        break
                                    elif custom_input == "2":
                                        sc.edit_custom_settings("sentence-newline", False)
                                        print(green + "\nSetting sentence-newline has updated to: False" + end_color)
                                        input("\nPress enter to go back to Edit Customized settings menu...")
                                        break
                                    print("\nThat is not a valid choice.")
                            elif change_setting == "2":
                                while True:
                                    print(blue + "\nEditing comment-space\n" + end_color)
                                    custom_input = input(" Enter a value --> ")
                                    if custom_input.isnumeric():
                                        sc.edit_custom_settings("comment-space", int(custom_input))
                                        print(green + "\nSetting comment-space has updated to: " + str(custom_input) + end_color)
                                        input("\nPress enter to go back to Edit Customized settings menu...")
                                        break
                                    print("\nThat is not a valid choice.")
                            elif change_setting == "3":
                                while True:
                                    print(blue + "\nEditing emptylines\n" + end_color)
                                    custom_input = input(" Enter a value --> ")
                                    if custom_input.isnumeric():
                                        sc.edit_custom_settings("emptylines", int(custom_input))
                                        print(green + "\nSetting emptylines has updated to: " + str(custom_input) + end_color)
                                        input("\nPress enter to go back to Edit Customized settings menu...")
                                        break
                                    print("\nThat is not a valid choice.")
                            elif change_setting == "q":
                                break
                            print("\nThat is not a valid choice.")
                            input("\nPress enter to go back to Edit Customized settings menu...")

                    elif choiceRule == "2":
                        sc.set_settings()
                        print(green + "\nSettings has updated to use Customized Settings" + end_color)
                        input("\nPress enter to go back to main menu...")
                        break
                    else:
                        raise KeyError
                except KeyError:
                    print("\nThat is not a valid choice.")
                    input("\nPress enter to go back to rule menu...")

        elif choice == "3":
            """
            Linter
            """
            break

        elif choice == "q":
            print("Thank you for using FalkenDev LaTeX Linter.")
            break

        else:
            print("\nThat is not a valid choice. Please choose from the menu.\n")
            input("Press enter to continue...")

if __name__ == "__main__":
    main()
