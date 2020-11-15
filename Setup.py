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
        settings_file.write(f"\nSERVER = \"{addr}\" \nPORT = {port} \n"+default)

info = {'server': "Clash of Code - Server", 'client': "Clash of Code"}
for i in info:
    target = f"{os.getcwd()}\\{i}\\{i}.exe"
    wDir = f"{os.getcwd()}\\{i}"
    icon = f"{os.getcwd()}\\{i}\\assets\\logo.ico"
    print(f"[{i}] [BUILDING SHORTCUT] {target}")
    mkshortcut(target, wDir, icon, info[i])
    print(f"[{i}] Completed")

default = '''
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
port = input("[Press enter to use default] Port to be used: ")

# set_server(socket.gethostbyname(socket.gethostname()), 6969)
set_server(server, port)
