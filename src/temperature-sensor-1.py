import random
import time
import paho.mqtt.client as mqtt

broker_address = "mqtt-broker"
broker_port = 1883
topic = "sensor/temperature"

def generate_temperature():
    return random.randint(-40, 140)

client = mqtt.Client()

client.connect(broker_address, broker_port, 60)

temperature = generate_temperature()
print(f"Sending temperature: {temperature}")
client.publish(topic, str(temperature))
