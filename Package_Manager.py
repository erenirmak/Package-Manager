
import installer
import updater

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

flag = 0
while flag == 0:
    selection = int(input("1. Install package(s)\n2. Update all packages\n3. Exit\n"))

    if selection == 1:
        installer.package_installer()
        flag = exit()

    elif selection == 2:
        updater.updater()
        flag = exit()

    elif selection == 3:
        flag = exit()

    else:
        print("Undefined selection!")
        flag = exit()