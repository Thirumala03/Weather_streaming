import paho.mqtt.client as mqtt

MQTT_BROKER = "localhost"
MQTT_TOPIC = "weather"

def publish_weather(data):
    client = mqtt.Client()
    client.connect(MQTT_BROKER)
    client.publish(MQTT_TOPIC, str(data))
    client.disconnect()
