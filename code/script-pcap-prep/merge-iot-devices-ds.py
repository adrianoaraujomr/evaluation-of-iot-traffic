#!/bin/python3

import os 
import numpy as np
import pandas as pd

# Pega os csvs que contem cada um dos dispositvos e junta em um novo dataset com duas colunas a mais (mac do dispositivo e sua classe de iot)

classes = {
    "44:65:0d:56:cc:d3" : "Controller/HUBS",
    "d0:52:a8:00:67:5e" : "Controller/HUBS",
    "30:8c:fb:2f:e4:b2" : "Cameras",
    "00:16:6c:ab:6b:88" : "Cameras",
    "00:24:e4:11:18:a8" : "Cameras",
    "f4:f2:6d:93:51:f1" : "Cameras",
    "30:8c:fb:b6:ea:45" : "Cameras",
    "00:24:e4:10:ee:4c" : "Cameras",
    "00:62:6e:51:27:2e" : "Cameras",
    "70:ee:50:18:34:43" : "Cameras",
    "ec:1a:59:79:f4:89" : "Energy Managment", 
    "74:c6:3b:29:d7:1d" : "Energy Managment",
    "d0:73:d5:01:83:08" : "Energy Managment",
    "50:c7:bf:00:56:39" : "Energy Managment",
    "00:24:e4:20:28:c6" : "Health Monitor",
    "70:ee:50:03:b8:ac" : "Health Monitor",
    "00:24:e4:1b:6f:96" : "Health Monitor",
    "18:b4:30:25:be:e4" : "Health Monitor",
    "74:6a:89:00:2e:25" : "Health Monitor",
    "ec:1a:59:83:28:11" : "Health Monitor",
    "70:5a:0f:e4:9b:c0" : "Appliences", 
    "e0:76:d0:33:bb:85" : "Appliences",
    "18:b7:9e:02:20:44" : "Appliences"
}

df = None

files = os.listdir("../datasets/original/iot-devices")
for file in files:
    if ".csv" in file:
        aux = file.replace("_",":").replace(".csv","")
        if aux in classes.keys():
            try:
                df_aux = pd.read_csv("../datasets/original/iot-devices/" + file)
                df_aux['Device MAC']   = aux
                df_aux['Device Class'] = classes[aux]
                if df is None:
                    df = df_aux
            except:
                pass
            else:
                df = pd.concat([df, df_aux])
                
df.to_csv("../datasets/original/iotPerDevice.csv")