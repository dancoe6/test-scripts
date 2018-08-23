from powerOutage import *
from api import *

durationOff = eval(input("Off duration: "))
durationOn = eval(input("On duration: "))
cycles = eval(input("Cycles (0 will run indefinitely: "))
if(cycles == 0):
    print("Test will run indefinitely with ",durationOff," seconds on and",durationOn,"seconds off.")
else:
    print("Test will run for",cycles," cycles with ",durationOff," seconds on and",durationOn,"seconds off.")
power_outage(durationOff,durationOn,cycles)