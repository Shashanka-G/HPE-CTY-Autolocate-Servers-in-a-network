import csv
with open("devices.csv",'r') as file:
    devices = file.readlines()
    device_list = []
    for device in devices:
        device_attributes = device.split(",")
        device_list.append(device_attributes)
    print(device_list)