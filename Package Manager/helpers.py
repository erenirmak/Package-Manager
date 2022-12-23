
import PySimpleGUI as sg
from manager import *

# variables
pip_process = {"install" : "pkg_inst",
               "info" : "pkg_info",
               "update" : "pkg_upd",
               "update_all" : "pkg_all",
               "search" : "pkg_src",
               "uninstall" : "pkg_uninst"}

pip_process_keys_list = list(pip_process.keys())

#process_pkgs = {"install" : PackageManager.installer(package, version),
#                "info" : PackageManager.pkg_info(package),
#                "update" : PackageManager.installer(package),
#                "update_all" : PackageManager.updater(),
#                "search" : PackageManager.searcher(src),
#                "uninstall" : PackageManager.uninstaller()}

# functions
def get_version_input(window):
    layout = [
        [sg.Text("Package version")],
        [sg.InputText(key = "version")],
        [sg.Button("OK"), sg.Button("CANCEL")]
    ]

    win = sg.Window("Version", layout, modal=True, grab_anywhere=True, enable_close_attempted_event=True)

    event, value = win.read()
    if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT:
        event = "CANCEL"

    win.close()
    window.write_event_value(event, None)

    return value["version"]

def make_disabled(window, pkg_key_name):
    for x in list(pip_process.values()):
        if x != "pkg_all":
            if x == pkg_key_name:
                window[x].update(disabled = False)
            else:
                window[x].update("", disabled = True)

    return pkg_key_name

def process_mapping(op, p, v):
    pkg_manager = PackageManager()
    
    if op == "install":
        end_job = pkg_manager.installer(p, v)
    elif op == "info":
        end_job = pkg_manager.pkg_info(p)
    elif op == "update":
        end_job = pkg_manager.installer(p)
    elif op == "update_all":
        end_job = pkg_manager.updater()
    elif op == "search":
        end_job = pkg_manager.searcher(p)
    elif op == "uninstall":
        end_job = pkg_manager.uninstaller(p)
    
    return end_job

# classes
#class Unbuffered(object):
#    def __init__(self, window):
#        self.window = window
#    def write(self, data):
#        self.window.write_event_value("OUT", data)
#    def writelines(self, datas):
#        self.window.write_event_value("OUT", ''.join(datas))