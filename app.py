from flask import Flask,render_template
import csv

app = Flask(__name__)

@app.route('/')

def index():
    with open("devices.csv",'r') as file:
        devices = file.readlines()
        device_list = []
        for device in devices:
            device_attributes = device.split(",")
            device_list.append(device_attributes)
        print(device_list)

    return render_template("index.html",devices=device_list)

if __name__ == '__main__':
    app.run(debug=True)

app.static_folder = 'static'


