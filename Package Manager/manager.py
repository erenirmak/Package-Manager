import subprocess
import os

class PackageManager(object):
    def __init__(self): #, pkg, version = None
        self.pkgs = []

    def pkg_list(self):
        os.chdir(".")

        subprocess.call("pip list > packages.txt", shell = True)

        with open("packages.txt") as f:
            for i, line in enumerate(f):
                if i == 0 or i == 1:
                    pass
                else:
                    self.pkgs.append(line.split(' ')[0])

        os.remove("packages.txt")

    def installer(self, package, version = None):
        try:
            if version == None: # update single package or install latest version
                subprocess.call("python -m pip install --upgrade " + package, shell = True)

            else: # install selected version
                subprocess.call("python -m pip install --upgrade " + package + "==" + version, shell = True)

            return True, 1

        except Exception as e:
            return (False, e)

    def uninstaller(self, package):
        try:
            subprocess.call("python -m pip uninstall " + package, shell = True)
            return True, 1

        except Exception as e:
            return False, e

    def searcher(self, src):
        self.pkg_list()

        try:            
            possible_pkgs = []
            for pkg in self.pkgs:
                if src in pkg:
                    possible_pkgs.append(pkg)

            return True, possible_pkgs
        
        except Exception as e:
            return False, e

    def pkg_info(self, package):
        try:
            subprocess.call("python -m pip show " + package, shell = True)            
            return True, 1

        except Exception as e:
            return False, e

    def updater(self): # all packages
        try:
            self.pkg_list()
            for pkg in self.pkgs:
                subprocess.call("pip install --upgrade " + pkg, shell = True)
            return True, 1

        except Exception as e:
            return False, e

    


