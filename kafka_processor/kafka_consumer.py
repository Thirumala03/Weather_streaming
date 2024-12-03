from kafka import KafkaConsumer
from database.mongodb_handler import insert_to_mongodb

KAFKA_TOPIC = "weather_topic"
KAFKA_BROKER = "localhost:9092"

consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=KAFKA_BROKER)

for message in consumer:
    weather_data = message.value.decode('utf-8')
    insert_to_mongodb(weather_data)
