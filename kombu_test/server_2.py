from kombu import Connection, Exchange, Queue, Consumer

rabbit_url = "amqp://mcos:bkcloud@localhost:5672/"

conn = Connection(rabbit_url)

exchange = Exchange("kombu-exchange", type="direct")

queue = Queue(name="kombu_queue_2", exchange=exchange, routing_key="BOB")
queue.maybe_bind(conn)
queue.declare()


def process_message(body, message):
    print("The body is {}".format(body))
    message.ack()


with Consumer(conn, queues=queue, callbacks=[process_message],
              accept=["text/plain"]):
    conn.drain_events()
