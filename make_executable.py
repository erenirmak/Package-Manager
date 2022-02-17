
import subprocess
import pkg_resources

subprocess.call("pip install --upgrade pyinstaller", shell = True)
print(pkg_resources.get_distribution("pyinstaller"))

subprocess.call("pyinstaller --onefile Package_Manager.py")