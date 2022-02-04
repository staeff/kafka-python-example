from json import dumps
from kafka import KafkaProducer
from loguru import logger

if __name__ == '__main__':
    # initializing the Kafka producer
    producer = KafkaProducer(
        bootstrap_servers = ['localhost:9092'],
        value_serializer = lambda x:dumps(x).encode('utf-8')
    )

    url = 'https://www.internetwache-polizei-berlin.de/vdb/Fahrraddiebstahl.csv'
    with open('Fahrraddiebstahl.csv') as infile:
        data = infile.readlines()
    logger.info('Sending data to kafka under topic name `biketheft`')
    for d in data:
        producer.send('biketheft', d)
        logger.info(f'Sending {d}')
