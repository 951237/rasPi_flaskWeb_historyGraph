from flask import Flask, request, render_template
import time
import datetime
import arrow

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/lab_temp")
def lab_temp():
	import sys
	import adafruit_dht
	dhtDevice = adafruit_dht.DHT22(board.D4)
    temperature = dhtDevice.temperature
    humidity = dhtDevice.humidity
	if humidity is not None and temperature is not None:
		return render_template("lab_temp.html", temp=temperature, hum=humidity)
	else:
		return render_template("no_sensor.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
