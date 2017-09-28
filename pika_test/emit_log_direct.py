#!/usr/bin/env python
import pika
import json
import sys

credentials = pika.PlainCredentials('mcos', 'bkcloud')
parameters = pika.ConnectionParameters('127.0.0.1',
                                       5672,
                                       '/',
                                       credentials)

connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

for i in range(1, 10):
    channel.basic_publish(exchange='direct_logs',
                          routing_key='info',
                          body=json.dumps({"Type": "info", "content": i}))
    print(" [x] Sent %r:%r" % ('info', str(i)))
connection.close()
