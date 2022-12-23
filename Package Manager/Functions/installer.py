import subprocess

def get_package_info():
    package_name = input("Package name to install: ")
    package_version = input("Package version (enter 0 for the latest available version): ")
    return package_name, package_version

def new_install():
    answer = int(input("\nWant to install another package?\n1. Yes\n2. No\n"))
    return answer - 1

def package_installer():
    flag = 0
    while flag == 0:
        package_name, package_version = get_package_info()

        if package_version == "0":
            subprocess.call("python -m pip install --upgrade " + package_name, shell = True)
            flag = new_install()

        else:
            subprocess.call("python -m pip install --upgrade " + package_name + "==" + package_version, shell = True)
            flag = new_install()
    
    input("Installation(s) are completed.")