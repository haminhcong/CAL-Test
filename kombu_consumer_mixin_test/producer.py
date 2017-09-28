import sys
import logging
from kombu.mixins import ConsumerMixin
from kombu import Connection, Exchange, Queue, Consumer, Producer
from kombu.utils.debug import setup_logging

from mcos_conf import TRANSPORT_URL, TRANSPORT_EXCHANGE, \
    MCOS_CLUSTER_NAME

QUEUE_PREFIX = 'cluster_status_queue_'
CLUSTER_STATUS_ROUTING_KEY = 'cluster_status'

if __name__ == "__main__":
    setup_logging(loglevel=logging.DEBUG)
    conn = Connection(TRANSPORT_URL, heartbeat=4)
    channel = conn.channel()
    exchange = Exchange(TRANSPORT_EXCHANGE, type="direct")
    producer = Producer(exchange=exchange, channel=channel,
                        routing_key=CLUSTER_STATUS_ROUTING_KEY)
    for i in range(1, 10):
        producer.publish({"Cluster": MCOS_CLUSTER_NAME, "Status": "Active"})
    sys.exit(1)
