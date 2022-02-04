# Kafka with kafka-python

This project shows how to run and explore Kafka locally using Docker and
how to interact with if using [kafka-python](https://github.com/dpkp/kafka-python).

This project needs `Kafka` (made available through a docker) and a Python environment with dependencies installed.
We connect to kafka using [kafka-python](https://github.com/dpkp/kafka-python). `producer.py` reads a csv file
and sends it into kafka under the topic `logs`. `consumer.py` gets the data from the topic `logs` and prints it out.

Example data is https://www.internetwache-polizei-berlin.de/vdb/Fahrraddiebstahl.csv

To set up everything run:

```sh
    $ make bootstrap
```

On the first run this will take a bit of time, because the docker images need to be downloaded.
When everything is ready, you need to open two terminal windows in the project folder, one runs the
producer, the other one runs the consumer.

Shell 1

```sh
    make consum
```

Shell 2

```sh
    make produce
```


## Exploring Kafka

Following https://developer.confluent.io/quickstart/kafka-docker/ to explore a local, dockerized installation of Kafka.

### Start the service(s)

Docker compose starts two services `broker` and `zookeeper`. `broker` has port `9092` and we will interact with Kafka
by sending commands to the `broker` service.

```sh
    $ docker-compose up -d
    $ docker ps
    CONTAINER ID   IMAGE                             COMMAND                  CREATED          STATUS          PORTS                          NAMES
    3a43635bf400   confluentinc/cp-kafka:6.2.0       "/etc/confluent/dock…"   29 minutes ago   Up 29 minutes   0.0.0.0:9092->9092/tcp         broker
    c7304373382e   confluentinc/cp-zookeeper:6.2.0   "/etc/confluent/dock…"   29 minutes ago   Up 29 minutes   2181/tcp, 2888/tcp, 3888/tcp   zookeeper
```

### Create a topic

It’s good practice to explicitly create topics before using them. Otherwise Kafka would automagically create them when referenced.

```sh
    $ docker exec broker kafka-topics --bootstrap-server broker:9092 --create --topic quickstart
    Created topic quickstart.
```

### Write messages to topics

Open an interactive prompt in the `broker` container and manually create a few messages.

```sh
    docker exec --interactive --tty broker kafka-console-producer --bootstrap-server broker:9092 --topic quickstart
```

### Read messages from the topic

And read the messages out.

```sh
    docker exec --interactive --tty broker kafka-console-consumer --bootstrap-server broker:9092 --topic quickstart --from-beginning
```

REPEAT AD INFINITUM. Kafka is so much funs!
