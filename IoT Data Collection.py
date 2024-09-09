# iot_data_collector.py
import paho.mqtt.client as mqtt
import json
import pandas as pd

class IoTDataCollector:
    def __init__(self, broker, port):
        self.client = mqtt.Client()
        self.client.connect(broker, port)
        self.client.on_message = self.on_message
        self.client.subscribe("process/sensor_data")
        self.data = []

    def on_message(self, client, userdata, message):
        data = json.loads(message.payload.decode())
        self.data.append(data)
        # Optional: Store in a database
        print(f"Received data: {data}")

    def start(self):
        self.client.loop_start()

    def get_data(self):
        return pd.DataFrame(self.data)
