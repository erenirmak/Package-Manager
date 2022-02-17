import subprocess

def get_package_info():
    package_name = input("Package name to install: ")
    package_version = input("Package version (enter 0 for the latest available version): ")
    return package_name, package_version

def package_installer(package_name, package_version = "0"):
    flag = 0
    while flag == 0:        
        if package_version == "0":
            subprocess.call("python -m pip install --upgrade " + package_name, shell = True)
            flag = int(input("\nWant to install another package?\n1. Yes\n2. No\n"))
            flag = flag - 1
        else:
            subprocess.call("python -m pip install --upgrade " + package_name + "==" + package_version, shell = True)
            flag = int(input("\nWant to install another package?\n1. Yes\n2. No\n"))
            flag = flag - 1
    
    input("Installation(s) are completed.")