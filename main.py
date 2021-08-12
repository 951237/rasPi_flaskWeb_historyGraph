from app import app, db

import adafruit_dht
import board

from model import *
from view import *

def app_init():
    db = DHTData()
    dhtDevice = adafruit_dht.DHT22(board.D4)
    return db, dhtDevice

if __name__ == '__main__':
    db, dhtDevice = app_init()
    app.run()

