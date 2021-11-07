#!/usr/bin/python3

import os
import shutil

parent_folder = "/home/adriano/Projetos/pcaps"

def get_files(diretorio, file_ext=".csv"):
    csvs = []
    dirs = [diretorio]
    while len(dirs) > 0:
        current = dirs.pop()
        aux = os.listdir(current)
        csvs += [current + "/" + e for e in aux if "." in e]
        dirs += [current + "/" + e for e in aux if "." not in e]
    return csvs

def move_files(diretorio, files):
    diff = 0 
    for file in files:
        new_name = diretorio + "/" + ".".join(file.split("/")[-3:])
        
        if "bro" in new_name:
            new_name = new_name.replace("bro.", "")
        if "IoTScenarios" in new_name:
            new_name = new_name.replace("IoTScenarios.", "")
            
        shutil.move(file, new_name)

files = get_files(parent_folder, file_ext=".pcap")
move_files(parent_folder, files)

files = get_files(parent_folder, file_ext=".log")
move_files(parent_folder, files)