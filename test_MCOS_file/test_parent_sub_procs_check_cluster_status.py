"""
A python script which starts celery worker and auto reload it when any code change happens.
I did this because Celery worker's "--autoreload" option seems not working for a lot of people.
"""
import eventlet

eventlet.monkey_patch()
import time
import os
import subprocess
from sys import path
from os.path import abspath, dirname
import os
import signal

path.insert(0, os.getcwd())
print os.getcwd()
from mcos.sub_processes import manage as sub_procs_manage

global child_pid
child_pid = sub_procs_manage.start_periodic_check__clusters_status()


def kill_child():
    print child_pid
    if child_pid is None:
        pass
    else:
        os.kill(child_pid, signal.SIGTERM)


import atexit

atexit.register(kill_child)
print("done")
while True:
    print("main procs")
    time.sleep(5)
