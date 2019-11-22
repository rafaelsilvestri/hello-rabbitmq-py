import pika

""" Simple implementation of a RabbitMQ Basic Publish using pika"""
__author__ = "Rafael Silvestri"
__version__ = "1.0.0"
__email__ = "rafaelcechinel@gmail.com"

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

this = channel.queue_declare(queue='hello-rabbit-queue',
                             durable=True,
                             arguments={'x-message-ttl': 60000})

while True:
    message = input("Enter a message [or enter to exit]: ")
    if not message.strip():
        break

    channel.basic_publish(exchange='',
                          routing_key='hello-rabbit-queue',
                          body=message)

    print(" [x] Message Sent!")

connection.close()
print("Connection closed!")
