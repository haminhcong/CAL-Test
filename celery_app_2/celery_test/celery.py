from __future__ import absolute_import, unicode_literals
from kombu import Exchange, Queue
from celery import Celery

app = Celery(str('celery_test'),
             broker='amqp://mcos:bkcloud@localhost',
             backend='rpc://',
             include=['celery_test.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)
app.conf.task_routes = {
    'celery_test.tasks.add': {'queue': 'add_queue_cluster_2'}}
app.conf.task_queues = (
    # Queue('feed_tasks',    routing_key='feed.#'),
    # Queue('regular_tasks', routing_key='task.#'),
    Queue('add_queue_cluster_2',
          exchange=Exchange('celery_test', type='direct'),
          routing_key='add_task'),
)
if __name__ == '__main__':
    app.start()
