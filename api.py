import requests
import json
import os
headers = {}
def get_user_id(token="11b23b5232364c6484469d60f9161ec4"):
    global headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer "+ token
    }
    response = requests.get("https://api.artik.cloud/v1.1/users/self",headers=headers)
    return json.loads(response.content)["data"]["id"]

def get_device_ids(user_id):
    response = requests.get("https://api.artik.cloud/v1.1/users/"+user_id+"/devices?count=100&includeProperties=false&includeShareInfo=false",headers=headers)
    device_data = json.loads(response.content)["data"]["devices"]
    device_dict = {}
    for element in device_data:
        manifest = element["manifestVersion"]
        if manifest == 1 or manifest == 4 :
            pass
        else:
            device_dict.update({element["id"]:{"name":element["name"]}})
    return device_dict

def get_device_statuses(device_dict):
    device_string = ""
    for element in device_dict:
        device_string = device_string + element + "%2C%20"
    response = requests.get("https://api.artik.cloud/v1.1/devices/status?dids="+device_string+"&includeSnapshotTimestamp=false&includeSnapshot=false",headers=headers)
    device_statuses = json.loads(response.content)["data"]
    for element in device_statuses:
            device_id = element["did"]
            device_status = element["data"]["availability"]
            device_dict[device_id].update({"status":device_status})
    return device_dict