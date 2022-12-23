
import subprocess

def package():
    package_name = input("Package name to show info: ")
    return package_name

def new_display():
    answer = int(input("\nWant to display another package?\n1. Yes\n2. No\n"))
    return answer - 1

def display_info():
    flag = 0
    while flag == 0:
        pkg = package()
        subprocess.call("pip show" + pkg, shell = True)

        flag = new_display()