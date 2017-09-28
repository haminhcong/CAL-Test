from __future__ import absolute_import, unicode_literals
from kombu import Exchange, Queue

# ^^^ The above is required if you want to import from the celery
# library.  If you don't have this then `from celery.schedules import`
# becomes `proj.celery.schedules` in Python 2.x since it allows
# for relative imports by default.

# Celery settings

broker_url = 'amqp://mcos:bkcloud@localhost'

#: Only add pickle to this list if your broker is secured
#: from unwanted access (see userguide/security.html)
accept_content = ['json',]
result_backend = 'rpc://'
task_serializer = 'json'
include = ['celery_server.tasks']
task_routes = {
    'celery_server.tasks.add_cluster': {'queue': 'add_queue_cluster_1',
                              'exchange': 'celery_server_ex',
                              'routing_key': 'add_cluster',
                              }}

task_queues = (
    # Queue('feed_tasks',    routing_key='feed.#'),
    # Queue('regular_tasks', routing_key='task.#'),
    Queue('add_queue_cluster_1',
          exchange=Exchange('celery_server_ex', type='direct'),
          routing_key='add_cluster'),
)