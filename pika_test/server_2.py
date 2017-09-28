#!/usr/bin/env python
import pika
import sys
import time

credentials = pika.PlainCredentials('mcos', 'bkcloud')
parameters = pika.ConnectionParameters('127.0.0.1',
                                       5672,
                                       '/',
                                       credentials)

connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

result = channel.queue_declare(exclusive=True, queue='server_2_queue')
queue_name = result.method.queue

channel.queue_bind(exchange='direct_logs',
                   queue=queue_name,
                   routing_key='info')

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    time.sleep(10)
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
