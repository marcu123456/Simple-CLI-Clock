from datetime import datetime
from time import sleep
import os
import sys

while True:
    try:
        now = datetime.now()
        timeCurrent = now.strftime("%H:%M:%S")

        print(timeCurrent)

    
        sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
    except KeyboardInterrupt:
        sys.exit(0)

    

    

