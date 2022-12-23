
from manager import PackageManager

def exit():
    exit_choice = input("\nWant to exit?\n1. Yes\n2. No\n")

    if exit_choice == "1" or exit_choice.lower() == "yes":
        input("Thank you for using my program.\nPress Enter to exit.")
        return 1
    
    elif exit_choice == "2" or exit_choice.lower() == "no":
        return 0
    
    else:
        input("Undefined selection.\nProgram will be terminated.")
        return 1

while (1):
    selection = int(input("1. Install package(s)\n2. Show package info\n3. Uninstall package(s)\n4. Update all packages\n5. Exit\n"))

    manager_handler = PackageManager(selection)

    del manager_handler

    if selection == 5:
        exit_handler = exit()
        if exit_handler:
            break
        else:
            continue