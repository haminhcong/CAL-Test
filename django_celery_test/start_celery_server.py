"""
A python script which starts celery worker and auto reload it when any code change happens.
I did this because Celery worker's "--autoreload" option seems not working for a lot of people.
"""

import time
# from watchdog.observers import Observer  ##pip install watchdog
# from watchdog.events import PatternMatchingEventHandler
# import psutil  ##pip install psutil
import os
import subprocess
from sys import path
from os.path import abspath, dirname

# path.insert(0, os.getcwd())
from .celery import app

current_wd = os.getcwd()
celery_working_dir = os.getcwd() + "/celery_sub_process"
celery_cmdline = 'celery worker -A celery_server -l INFO'.split(" ")


def run_worker():
    print("Ready to call {} ".format(celery_cmdline))
    os.chdir(celery_working_dir)
    subprocess.Popen(celery_cmdline)
    print("Done callling {} ".format(celery_cmdline))
    os.chdir(current_wd)
    print os.getcwd()

if __name__ == "__main__":
    run_worker()
    print("done")
