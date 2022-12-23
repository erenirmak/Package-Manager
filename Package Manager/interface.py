
import PySimpleGUI as sg
from helpers import *

# main interface
layout = [[sg.Column([
                [sg.Radio("Install Package", 1, enable_events = True, key = "install")],
                [sg.Radio("Show Package Info", 1, enable_events = True, key = "info")],
                [sg.Radio("Update Package", 1, enable_events = True, key = "update")],
                [sg.Radio("Update All Packages", 1, enable_events = True, key = "update_all")],
                [sg.Radio("Package Search", 1, enable_events = True, key = "search")],
                [sg.Radio("Uninstall Package", 1, enable_events = True, key = "uninstall")],
                [sg.Button("Execute")]]),
          sg.Column([
                [sg.InputText(disabled = True, disabled_readonly_background_color="Gray", pad = (0, 5), key = "pkg_inst")],
                [sg.InputText(disabled = True, disabled_readonly_background_color="Gray", pad = (0, 5), key = "pkg_info")],
                [sg.InputText(disabled = True, disabled_readonly_background_color="Gray", pad = (0, 5), key = "pkg_upd")],
                [sg.InputText(disabled = True, disabled_readonly_background_color="Gray", pad = (0, 5), key = "pkg_all")],
                [sg.InputText(disabled = True, disabled_readonly_background_color="Gray", pad = (0, 5), key = "pkg_src")],
                [sg.InputText(disabled = True, disabled_readonly_background_color="Gray", pad = (0, 5), key = "pkg_uninst")],
                [sg.Button("Cancel")]]),

          sg.Column([[sg.Multiline("", size=(80, 20), auto_refresh = True, write_only = True, autoscroll=True,
                         reroute_stdout=True, reroute_stderr=True, reroute_cprint = True, key='output')]])
          ]]

window = sg.Window("Package Manager", layout, finalize = True)

# event loop
while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == "Cancel":
        break
    
    # divide values dict into radio and inputtext
    radio_values = {}
    text_values = {}
    for k, v in values.items():
        if "pkg" not in k:
            radio_values[k] = v
        else:
            text_values[k] = v

    # check radio values, determine related inputtext to make it activated, others disabled
    for k, v in radio_values.items():
        if v == True:
            input_key = make_disabled(window, pip_process[k])

    # new package install - determine version, if not install, get process & package name
    pkg_version = None
    if event == "Execute":
        if radio_values["install"] == True:
            pkg_version = get_version_input(window)        
        
        if pkg_version == "":
            pkg_version = None

        ######### problematic ##########
        process_pkg = {}
        for k, v in radio_values.items():
            if v == True:
                process_pkg[k] = text_values[pip_process[k]]

        result = process_mapping(str(list(process_pkg.keys())[0]), str(list(process_pkg.values())[0]), pkg_version)
        process_pkg.clear()
    
window.close()


