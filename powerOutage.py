import requests
import time
import os
import webbrowser
import csv
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
    testStartTime = 'Test '+strftime("%Y-%m-%d %H:%M", localtime())
    if cycles == 0:
        indefinite = True
    else:
        indefinite = False
    sampleTimes = []
    deviceStatus = []
    plot_url = ""
    first_loop = True
    while (cycles > 0 or indefinite):
        turn_off()
        time.sleep(durationOff)
        turn_on()
        time.sleep(durationOn)
        cycles-=1
        device_dict = get_device_statuses(get_device_ids(get_user_id()))
        if(first_loop):
            with open('test.csv','w') as f:
                w = csv.writer(f,lineterminator = '\n')
                did= ['']
                for element in device_dict:
                    did.append(element)
                w.writerow(did)
                name= ['']
                for element in device_dict:
                    name.append((device_dict[element]['name']))
                w.writerow(name)
                status= [strftime("%Y-%m-%d %H:%M:%S", localtime())]
                for element in device_dict:
                    status.append((device_dict[element]['status']))
                w.writerow(status)
            first_loop = False
        else:
            with open('test.csv','a') as f:
                w = csv.writer(f,lineterminator = '\n')
                status= [strftime("%Y-%m-%d %H:%M:%S", localtime())]
                for element in device_dict:
                    status.append((device_dict[element]['status']))
                w.writerow(status)
        # sampleTimes.append(strftime("%a, %b %d %Y %H:%M:%S", localtime()))
        # deviceStatus.append(statuses)







