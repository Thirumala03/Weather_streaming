from kafka import KafkaProducer
import paho.mqtt.client as mqtt

KAFKA_BROKER = "localhost:9092"
KAFKA_TOPIC = "weather_topic"

producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER)

def on_message(client, userdata, msg):
    producer.send(KAFKA_TOPIC, msg.payload)

def setup_mqtt():
    client = mqtt.Client()
    client.on_message = on_message
    client.connect("localhost")
    client.subscribe("weather")
    client.loop_forever()
