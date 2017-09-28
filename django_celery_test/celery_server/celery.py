from __future__ import absolute_import, unicode_literals
import os
# Create your tasks here
import os
import django
import time
import memcache
from sys import path
from os.path import abspath, dirname
path.insert(0, os.path.dirname(os.getcwd()))

from celery import Celery
import memcache

app = Celery('celery_server')
app.config_from_object('celery_server.settings')

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
