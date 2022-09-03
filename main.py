"""
Main.py
"""
from src.menu import menustart, menufile, menurule
from src.input import Input
from src.rules import Rules

def main():
    """
    Main
    """
    input_class = Input()
    rules_class = Rules()
    while True:
        menustart()

        choice = input(" Enter a action --> ")

        if choice == "1":
            """
            Change file
            """
            while True:
                menufile()
                choiceFile = input(" Enter a action --> ")
                try:
                    if choiceFile == "q":
                        break
                    elif choiceFile == "1":
                        break # Maybe implement this | Sooner
                    elif choiceFile == "2":
                        new_file = input("Enter the file --> ")
                        input_class.load_file(new_file)
                        input_class.open_file()
                        input(" Enter a action --> ")

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
                data = rules_class.read_json()
                menurule(data)
                choiceRule = input(" Enter a action --> ")
                try:
                    if choiceRule == "q":
                        break
                    elif choiceRule == "1":
                        rules_class.read_json()
                        change_rule = input("Input which rule u want to change --> ")
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
