from flask import render_template

from app import app
from model import SensorReading

@app.route('/')
def homepage():
    import adafruit_dht
    import board

    dhtDevice = adafruit_dht.DHT22(board.D4)

    temperature = dhtDevice.temperature
    humidity = dhtDevice.humidity

    return render_template('lab_temp.html', temp = temperature, hum = humidity)

@app.route('/graph')
    return render_template('graph.html')
