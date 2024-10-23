import psutil
import time
import subprocess

while True:
    battery = psutil.sensors_battery()
    if battery.power_plugged:
        print("Charger connected")
    else:
        print ("Charger not connected")
        # subprocess.call("shutdown -s -t 0", shell=True) <== This will shutdown your pc.
        # For Linux/Mac, use: subprocess.call("shutdown -h now", shell=True)
    time.sleep(3)
    subprocess.call("cls",shell=True)
    # You can use subprocess.call("clear", shell=True) for linux distros
    
