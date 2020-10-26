import requests
import json
import sys
import os
def start_server():
    if (sys.platform.startswith("win32")):
        os.system("start /B java -jar runTodoManagerRestAPI-1.5.5.jar")
    else:
        os.system("java -jar runTodoManagerRestAPI-1.5.5.jar")
    os.system("sleep 2s") 
    
def shutdown_server():
     os.system("curl --location --request GET 'localhost:4567/shutdown'")

def restart():
    shutdown_server()
    start_server() 
#MAIN
shutdown_server()

