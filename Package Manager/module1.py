
#row1 = [[sg.Radio(pip_process[0], 1, enable_events = True, key = "install")],
#        [sg.Radio(pip_process[1], 1, enable_events = True, key = "info")],
#        [sg.Radio(pip_process[2], 1, enable_events = True, key = "update")],
#        [sg.Radio(pip_process[5], 1, enable_events = True, key = "update_all")],
#        [sg.Radio(pip_process[3], 1, enable_events = True, key = "search")],
#        [sg.Radio(pip_process[4], 1, enable_events = True, key = "uninstall")],
#        [sg.Button("OK")]]

#row2 = [[sg.InputText(pad = (0, 5), disabled = True, key = "pkg_inst")],
#        [sg.InputText(pad = (0, 5), disabled = True, key = "pkg_info")],
#        [sg.InputText(pad = (0, 5), disabled = True, key = "pkg_upd")],
#        [sg.InputText(pad = (0, 5), disabled = True, key = "pkg_all")],
#        [sg.InputText(pad = (0, 5), disabled = True, key = "pkg_src")],
#        [sg.InputText(pad = (0, 5), disabled = True, key = "pkg_uninst")],
#        [sg.Button("Cancel")]]

#layout = [ [sg.Frame( layout = row1, title = '', border_width = 0.1 ),
#            sg.Frame( layout = row2, title = '', border_width = 0.1 ) ] ]


    #    window["pkg_inst"].update(disabled = False)
    #    window["pkg_info"].update(disabled = True)
    #    window["pkg_upd"].update(disabled = True)
    #    window["pkg_all"].update(disabled = True)
    #    window["pkg_src"].update(disabled = True)
    #    window["pkg_uninst"].update(disabled = True)


    
    #if values["install"] == True:
    #    input_key = make_disabled("pkg_inst")

    #elif values["info"] == True:
    #    input_key = make_disabled("pkg_info")

    #elif values["update"] == True:
    #    input_key = make_disabled("pkg_upd")

    #elif values["update_all"] == True:
    #    input_key = make_disabled("pkg_all")

    #elif values["search"] == True:
    #    input_key = make_disabled("pkg_src")

    #elif values["uninstall"] == True:
    #    input_key = make_disabled("pkg_uninst")



    
    #def searcher(self):
        #os.chdir(".")

        #subprocess.call("pip list > packages.txt", shell = True)

        #with open("packages.txt") as f:
        #    package_list = []
        #    for i, line in enumerate(f):
        #        if i == 0 or i == 1:
        #            pass
        #        else:
        #            package_list.append(line.split(' ')[0])

        #os.remove("packages.txt")