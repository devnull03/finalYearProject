import os, winshell
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

info = {'server': "Clash of Code - Server", 'client': "Clash of Code"}

for i in info:
    target = f"{os.getcwd()}\\{i}\\{i}.py"
    wDir = f"{os.getcwd()}\\{i}"
    icon = f"{os.getcwd()}\\{i}\\assets\\logo.ico"
    mkshortcut(target, wDir, icon, info[i])
