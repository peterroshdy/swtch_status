import sys
import time
import napalm
import os
import json
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
    dev_type = 'ios'
    dev_creds={
    'hostname': 'xx.xx.xx.xx',
    'username': 'xxxx',
    'password': 'xxxx',
    } # Use a dictionary for the login parameters
    
    driver = napalm.get_network_driver(dev_type)
    conn = driver(**dev_creds)
    conn.open()
    output33 = conn.get_interfaces()

    dev_creds31={
    'hostname': 'xx.xx.xx.xx',
    'username': 'xxxx',
    'password': 'xxxx',
    } # Use a dictionary for the login parameters
    
    driver31 = napalm.get_network_driver(dev_type)
    conn31 = driver31(**dev_creds31)
    conn31.open()
    output31 = conn31.get_interfaces()

    return render_template('home.html', interfaces31=output31,  interfaces33=output33)


if __name__ == '__main__':
    app.run(debug=True)