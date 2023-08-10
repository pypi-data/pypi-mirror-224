import os 
import pathlib
from os import * 
from pathlib import * 
import requests 
import subprocess
import platform


windows_root = "C:/Windows"
linux_root = "/"
mac_root = "/"

def find_all_files(root):
  for dir_path, _, files in os.walk(root):
    for file in files:
      print(os.path.join(dir_path, file))

def shell(code): 
    try: 
        os.system(code)
    except: 
        return "Error."

class Utils(): 

    def checkos():
        os = platform.system()
        if os == "Windows":
            return "Windows"
        elif os == "Linux":
            return "Linux"
        elif os == "Darwin":
            return "Mac"
        else:
            raise ValueError(f"Unknown operating system: {os}")

    def getroot(): 
        if Utils.checkos() == "Windows": 
            return windows_root
        elif Utils.checkos() == "Linux": 
            return linux_root
        elif Utils.checkos() == "Mac": 
            return mac_root
        else: 
            return "Unknown root."
        
    def find_all_files(root):
        for dir_path, _, files in os.walk(root):
            for file in files:
                print(os.path.join(dir_path, file))
