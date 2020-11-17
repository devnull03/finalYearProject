from client import settings
import os, winshell, sys
from win32com.client import Dispatch

desktop = winshell.desktop()

def mkshortcut(target, wDir, icon, link_name):
    path = os.path.join(desktop, f"{link_name}.lnk")
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = wDir
    shortcut.IconLocation = icon
    shortcut.save()

def set_server(addr, port):
    if port == "":
        port = settings.PORT
    with open("client/settings.py", "w") as settings_file:
        settings_file.write(f"import socket\n\nSERVER = \"{addr}\" \nPORT = {port} \n"+comment)

info = {'server': "Clash of Code - Server", 'client': "Clash of Code"}
for i in info:
    target = f"{os.getcwd()}\\{i}\\{i}.py"
    wDir = f"{os.getcwd()}\\{i}"
    icon = f"{os.getcwd()}\\{i}\\assets\\logo.ico"
    print(f"[{i}] [BUILDING SHORTCUT] {target}")
    mkshortcut(target, wDir, icon, info[i])
    print(f"[{i}] Completed")

comment = '''
# 
# Default config:
# 
# import socket
# SERVER = socket.gethostbyname(socket.gethostname())
# PORT = 6969 
# 
'''

server = input("[Press enter to skip] Server address: ")
if server == "":
    sys.exit()
elif server == "default":
    server = "socket.gethostbyname(socket.gethostname())"
    port = 6969
else:
    port = input("[Press enter to use default] Port to be used: ")

set_server(server, port)
