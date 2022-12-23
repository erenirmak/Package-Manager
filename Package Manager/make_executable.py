
import subprocess
import pkg_resources

subprocess.call("pip install --upgrade pyinstaller", shell = True)
print(pkg_resources.get_distribution("pyinstaller"))

excluded_modules_list = ['matplotlib', 'torch', 'nacl',
                         'tensorflow', 'PIL', 'beautifulsoup4',
                         'pyarrow', 'pygame', 'scipy', 'sympy',
                         'sklearn', 'pytube', 'opencv', 'lxml',
                         'pytest', 'numba', 'jedi', 'numpy',
                         'jinja2', 'llvmlite']

excluded_module_string = ''
for module in excluded_modules_list:
    excluded_module_string += f' --exclude-module {module}'

subprocess.call(f"pyinstaller --onefile {excluded_module_string} Package_Manager.py")