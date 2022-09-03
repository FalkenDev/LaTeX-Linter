"""
Main.py
"""
from src.menu import menustart, menufile, menurule

def main():
    """
    Main
    """
    while True:
        menustart()

        choice = input(" Enter a action --> ")

        if choice == "1":
            while True:
                menufile()
                choiceFile = input(" Enter a action --> ")
                try:
                    if choiceFile == "q":
                        break
                    else:
                        raise KeyError
                except KeyError:
                    print("\nThat is not a valid choice.")
                    input("\nPress enter to go back to rule menu...")

        elif choice == "2":
            while True:
                menurule()
                choiceFile = input(" Enter a action --> ")
                try:
                    if choiceFile == "q":
                        break
                    else:
                        raise KeyError
                except KeyError:
                    print("\nThat is not a valid choice.")
                    input("\nPress enter to go back to rule menu...")

        elif choice == "3":
            break

        elif choice == "q":
            print("Thank you for using FalkenDev LaTeX Linter.")
            break

        else:
            print("\nThat is not a valid choice. Please choose from the menu.\n")
            input("Press enter to continue...")

if __name__ == "__main__":
    main()
