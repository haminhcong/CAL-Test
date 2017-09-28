from kombu import Connection, Exchange, Producer, Queue

rabbit_url = "amqp://mcos:bkcloud@localhost:5672/"

conn = Connection(rabbit_url)

channel = conn.channel()

exchange = Exchange("kombu-exchange", type="direct")

producer = Producer(exchange=exchange, channel=channel, routing_key="BOB")

# queue = Queue(name="example-queue", exchange=exchange, routing_key="BOB")
# queue.maybe_bind(conn)
# queue.declare()


producer.publish("Hello there!")
