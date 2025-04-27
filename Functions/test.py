import os
import sys

def shutdown():
    print("Shutting down the system...")
    os.system('shutdown /s /f /t 0')  # This will initiate a shutdown on Windows
    sys.exit()

# To simulate shutdown
shutdown()
