import subprocess

def package():
    package = input("Package to uninstall: ")
    return package

def new_uninstall():
    answer = int(input("\nWant to install another package?\n1. Yes\n2. No\n"))
    return answer - 1

def uninstaller():
    flag = 0
    while flag == 0:
        pkg = package()
        subprocess.call("pip uninstall" + pkg, shell = True)

        flag = new_uninstall()