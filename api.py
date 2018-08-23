import requests
import json
import os
def get_device_statuses():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 11b23b5232364c6484469d60f9161ec4"
    }
    response = requests.get("https://api.artik.cloud/v1.1/users/self",headers=headers)
    user_id = json.loads(response.content)["data"]["id"]

    response = requests.get("https://api.artik.cloud/v1.1/users/"+user_id+"/devices?count=100&includeProperties=false&includeShareInfo=false",headers=headers)
    device_data = json.loads(response.content)["data"]["devices"]
    device_id = ""
    device_count = 0
    for element in device_data:
        manifest = element["manifestVersion"]
        if manifest == 1 or manifest == 4 :
            pass
        else:
            device_id = device_id + element["id"] + "%2C%20"
            device_count += 1
    if(device_count == 0):
        print("ERROR: No devices found on account")
        return "none"
    else:
        print (device_count,"devices found")

    response = requests.get("https://api.artik.cloud/v1.1/devices/status?dids="+device_id,headers=headers)
    device_statuses = json.loads(response.content)["data"]
    return device_statuses[0]["data"]["availability"]
    # online_count = 0
    # offline_count = 0
    # for element in device_statuses:
    #     status = element["data"]["availability"]
    #     if status == "online" :
    #         online_count += 1
    #     else:
    #         offline_count += 1