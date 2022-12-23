import subprocess
import os

def req_dir():
    # the directory to save the requirements
    requirements_dir = r"."
    os.chdir(requirements_dir)

def req_file():
    # save all the requirements into the .txt file to the given directory
    subprocess.call("pip list > requirements.txt", shell = True)

def req_file_processor():
    # open the requirements file and get the package names from the file
    with open("requirements.txt") as f:
        package_list = []
        for i, line in enumerate(f):
            if i == 0 or i == 1:
                pass
            else:
                package_list.append(line.split(' ')[0])
    
    #print(package_list)
    
    return package_list    

def updater():
    req_dir()
    req_file()
    package_list = req_file_processor()
    
    # update all packages in the requirements
    for pkg in package_list:
        subprocess.call("pip install --upgrade " + pkg, shell = True)

    input("Update(s) are completed.")