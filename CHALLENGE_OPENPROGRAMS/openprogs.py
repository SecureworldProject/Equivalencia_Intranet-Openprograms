from math import log10, sqrt

import os
from pathlib import Path
import time
#para instalar el modulo easygui simplemente:
#pip3 install easygui
# o bien py -m pip install easygui
import easygui 
#import lock

#pip3 install psutil
#o bien py -m pip install psutil
import psutil

#import socket
#import fnmatch
# variables globales
# ------------------
props_dict={} 
DEBUG_MODE=True

def init(props):
    global props_dict
    print("Python: Enter in init")
    
    #props es un diccionario
    props_dict= props

    return 0


def executeChallenge():
    print("Starting execute")
    
    #obtenemos lista real
    lista_progs=[]
    for i in psutil.process_iter():
        lista_progs.append(i.name())

    
    lista= props_dict["process_list"] # lista es un string con subcadenas separadas por ","
    print ("lista es", lista)
    lista=lista.replace(" ", "")
    lista =lista.split(",")
    cad=""
    for i in lista:
        if i in lista_progs:
            cad=cad+"1"
            continue
        else:
            cad=cad +"0"
    print ("cad:",cad)

    decimal = int(cad, 2)
    print("Número decimal:", decimal)
    
    key = bytes(cad,'utf-8')
    key_size = len(key)

    result =(key, key_size)
    print ("result:",result)
    return result



if __name__ == "__main__":
    # la lista de programas se puede cambiar:
    # chrome, notepad, teams ,
    # antivirus symantec "ccSvcHst.exe"
    # antivirus IPS utilities "sisipsutil.exe"
    # cisco user interface "vpnui.exe"
    # lenovo power management service "ibmpmsvc.exe"
    
    midict={"process_list": "chrome.exe,notepad.exe, Teams.exe,ccSvcHst.exe,sisipsutil.exe,vpnui.exe,ibmpmsvc.exe,MsSense.exe"} 

    init(midict)
    executeChallenge()

