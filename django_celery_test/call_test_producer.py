"""
A python script which starts celery worker and auto reload it when any code change happens.
I did this because Celery worker's "--autoreload" option seems not working for a lot of people.
"""

import time
import os
import subprocess
from sys import path
from os.path import abspath, dirname
import os
import signal

current_wd = os.getcwd()
proc = subprocess.Popen(
    ["../venv/bin/python", "django_celery/test_producer.py"])
global child_pid
child_pid = proc.pid


def kill_child():
    if child_pid is None:
        pass
    else:
        os.kill(child_pid, signal.SIGTERM)


import atexit

atexit.register(kill_child)
print("done")
time.sleep(5)
print("exit")
