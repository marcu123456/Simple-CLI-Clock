from datetime import datetime
from time import sleep
import os
import sys

def clear():
    os.system('clear')

# Windows check. So the thing doesn't brake.
if os.name == 'nt':
    print('Simple CLI-Clock does not support Windows.')
    sys.exit(1)

while True:
    try:
        now = datetime.now()
        timeCurrent = now.strftime("%H:%M:%S")

        print(timeCurrent)

        sleep(1)
        clear()
    except KeyboardInterrupt:
        sys.exit(0)

    

    

