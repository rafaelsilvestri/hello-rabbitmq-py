## About
This is a simple `Hello World` that uses RabbitMQ as a message broker and Python [Pika](https://github.com/pika/pika) 
client for AMQP protocol.


#### Setup
This setup assumes you already have [docker-compose](https://docs.docker.com/compose/) and [docker](https://www.docker.com/why-docker) installed.
```bash
git clone git@github.com:rafaelsilvestri/hello-rabbitmq-py.git
cd hello-rabbitmq-py
docker-compose up -d
```

Install Python3 and Pika using pip3
```bash
apt install python3
apt install python3-pip
pip3 install pika
```

#### Play
Open RabbitMQ Console by typing http://localhost:15672/ (or your container's ip)

The credentials are:
```
username: guest
password: guest
```

You can see `Queues` are empty.

##### Running
Open a terminal to start the `receiver` by typing the command bellow:
```bash
python3 receiver.py
```

To start publishing messages, open a new terminal and start the `sender` by typing the command bellow:
```bash
python3 sender.py
```

