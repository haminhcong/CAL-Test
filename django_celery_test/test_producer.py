from __future__ import absolute_import, unicode_literals
import time
import os
import subprocess
from sys import path
from os.path import abspath, dirname

# current_wd = os.getcwd()
# main_working_dir = os.path.dirname(os.getcwd())
# path.insert(0, os.path.dirname(os.getcwd()))
# os.chdir(main_working_dir)
# print path
path.insert(0, os.getcwd())
print os.getcwd()

# from celery_server import tasks
from celery_sub_process.celery_server import tasks

x = 12
tasks.add_cluster.delay(x, x + 1, x + 2)
#

