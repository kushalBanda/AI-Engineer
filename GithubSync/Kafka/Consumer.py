import json
from kafka import KafkaConsumer

def deserialize_json(data):
    if not data:
        return None
    try:
        return json.loads(data.decode('utf-8'))
    except (json.JSONDecodeError, UnicodeDecodeError):
        print(f"Warning: Failed to deserialize message: {data}")
        return None

# Define Kafka Consumer
consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers = ['localhost:9092'],
    auto_offset_reset = 'earliest',
    enable_auto_commit = True,
    value_deserializer = deserialize_json
)

# Consume messages with error handling for non-Json messages
for message in consumer:
    if message.value is not None:
        print(message.value)