from kafka import KafkaConsumer

producer = KafkaConsumer(
    bootstrap_servers = ['localhost:9092']
)

consumer = KafkaConsumer("biketheft")
consumer
for msg in consumer:
    print(msg)
