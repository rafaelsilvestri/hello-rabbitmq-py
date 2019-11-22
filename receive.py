import pika

""" Simple implementation of a RabbitMQ consumer using pika"""
__author__ = "Rafael Silvestri"
__version__ = "1.0.0"
__email__ = "rafaelcechinel@gmail.com"

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

this = channel.queue_declare(queue='hello-rabbit-queue',
                             durable=True,
                             arguments={'x-message-ttl': 60000})


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(
    queue='hello-rabbit-queue', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
