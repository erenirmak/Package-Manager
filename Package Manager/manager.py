import subprocess
import os

class PackageManager(object):
    def __init__(self, choice):
        self.choice = choice
        if self.choice == 1:
            self.installer()
        elif self.choice == 2:
            self.displayer()
        elif self.choice == 3:
            self.uninstaller()
        elif self.choice == 4:
            self.updater()
        elif self.choice == 5:
            pass
        else:
            print("Undefined choice!")

        self.do = "None"
        self.name = None

    def re_do(self):
        answer = int(input(f"\nWant to {self.do} another package?\n1. Yes\n2. No\n"))
        return answer - 1

    def installer(self):
        self.do = "install"

        flag = 0
        while flag == 0:
            self.name = input(f"Package name to {self.do}: ")
            package_version = input("Package version (enter 0 for the latest available version): ")
        
            if package_version == "0":
                subprocess.call("python -m pip install --upgrade " + self.name, shell = True)
                flag = self.re_do()

            else:
                subprocess.call("python -m pip install --upgrade " + self.name + "==" + package_version, shell = True)
                flag = self.re_do()
    
        input("Installation(s) are completed.")

    def uninstaller(self):
        self.do = "uninstall"        

        flag = 0
        while flag == 0:
            self.name = input(f"Package name to {self.do}: ")

            subprocess.call("python -m pip uninstall " + self.name, shell = True)
            flag = self.re_do()

    def displayer(self):
        self.do = "display"
        
        flag = 0
        while flag == 0:
            self.name = input(f"Package name to {self.do}: ")
            
            subprocess.call("python -m pip show " + self.name, shell = True)
            flag = self.re_do()

    def updater(self):
        self.do = "update"
        os.chdir(".")

        subprocess.call("pip list > requirements.txt", shell = True)

        with open("requirements.txt") as f:
            package_list = []
            for i, line in enumerate(f):
                if i == 0 or i == 1:
                    pass
                else:
                    package_list.append(line.split(' ')[0])

        os.remove("requirements.txt")

        for pkg in package_list:
            subprocess.call("pip install --upgrade " + pkg, shell = True)