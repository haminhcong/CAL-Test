import logging
from kombu.mixins import ConsumerMixin
from kombu import Connection, Exchange, Queue, Consumer
from kombu.utils.debug import setup_logging

from mcos_conf import TRANSPORT_URL, TRANSPORT_EXCHANGE, MCOS_CLUSTER_NAME

QUEUE_PREFIX = 'cluster_status_queue_'
CLUSTER_STATUS_ROUTING_KEY = 'cluster_status'


class Worker(ConsumerMixin):
    def __init__(self, connection, queues):
        self.connection = connection
        self.queues = queues

    def get_consumers(self, Consumer, channel):
        return [Consumer(queues=self.queues, callbacks=[self.handle_msg])]

    def handle_msg(self, body, message):
        print body['Cluster']
        print('Got task: {0!r}'.format(body))
        message.ack()


# def run_consumer_server(conn, queues):
#     print "Connecting ..."
#     with Connection(connection_string) as conn:
#
#         try:
#             worker = Worker(conn, queues)
#             worker.run()
#         except:
#             raise


if __name__ == "__main__":
    setup_logging(loglevel=logging.DEBUG)
    conn = Connection(TRANSPORT_URL, heartbeat=4)
    exchange = Exchange(TRANSPORT_EXCHANGE, type="direct")
    queues = [Queue(name=QUEUE_PREFIX + MCOS_CLUSTER_NAME, exchange=exchange,
                    routing_key=CLUSTER_STATUS_ROUTING_KEY), ]
    for queue in queues:
        queue.maybe_bind(conn)
        queue.declare()
    with conn:
        print "Connected."
        print "Awaiting tasks ..."
        try:
            worker = Worker(conn, queues)
            worker.run()
        except:
            raise
    sys.exit(1)
