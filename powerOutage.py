import requests
import time
import os
import webbrowser
from chart import *
from powerstripTest import *
from api import *

# powerOutage is a script that simulates a power outage for a given length
# of time using a relay-triggered powerstrip controlled by a raspberry pi.
# It takes two required inputs:
#   durationOff is the amount of time in seconds the power should stay off in each cycle
#   durationOn is the amount of time in seconds the power should stay on before checking device status
# and one optional input:
#   cycles is the number of times run (one cycle the on duration and off duration)
# Note that if cycles is not passed in, program will run indefinitely
# The function always turns power off to start and ends with power on
def power_outage(durationOff, durationOn, cycles=0):
    testStartTime = 'Test '+strftime("%a, %b %d %Y %H:%M", localtime())
    if cycles == 0:
        indefinite = True
    else:
        indefinite = False
    sampleTimes = []
    deviceStatus = []
    plot_url = ""
    while (cycles > 0 or indefinite):
        turn_off()
        time.sleep(durationOff)
        turn_on()
        time.sleep(durationOn)
        cycles-=1
        status = get_device_statuses()
        sampleTimes.append(strftime("%a, %b %d %Y %H:%M:%S", localtime()))
        deviceStatus.append(status)
        plot_url = create_chart(sampleTimes,deviceStatus, 'test') #use testStartTime
    os.startfile(plot_url)







