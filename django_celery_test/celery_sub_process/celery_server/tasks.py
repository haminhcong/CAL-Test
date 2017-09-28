from __future__ import absolute_import, unicode_literals
# Create your tasks here
import os
import django
import time
import memcache
from sys import path
from os.path import abspath, dirname

path.insert(0, os.path.dirname(os.getcwd()))
from .celery import app

os.environ['DJANGO_SETTINGS_MODULE'] = 'django_celery.settings'
django.setup()
from django_celery.apps.cluster.models import SystemCluster

# for cluster in SystemCluster.objects.all():
#     print cluster.id


@app.task(ignore_result=True)
def add_cluster(cluster_name, address_ip, address_port):
    print path
    print(
        "received: " + str(cluster_name) + ' - ' +
        str(address_ip) + ' - ' + str(address_port))
    try:

        new_system_cluster = SystemCluster(name=cluster_name,
                                           address_ip=address_ip,
                                           address_port=address_port)
        # client = memcache.Client([('127.0.0.1', 11211)])
        # client.incr('celery_server_counter')
        # print client.get("celery_server_counter")
        # time.sleep(client.get("celery_server_counter"))
        new_system_cluster.save()
    except Exception as e:
        print e


@app.task
def mul(x, y):
    return x * y
