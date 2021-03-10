from datetime import datetime
from time import sleep
import os
import sys

def windows():
    while True:
        try:
            now = datetime.now()
            timeCurrent = now.strftime("%H:%M:%S")

            print(timeCurrent)

            sleep(1)
            os.system('cls')
        except KeyboardInterrupt:
            sys.exit(0)

def unix():
    while True:
        try:
            now = datetime.now()
            timeCurrent = now.strftime("%H:%M:%S")

            print(timeCurrent)

            sleep(1)
            os.system('clear')
        except KeyboardInterrupt:
            sys.exit(0)

if os.name == 'nt':
    windows()
else:
    unix()
    



    

    

