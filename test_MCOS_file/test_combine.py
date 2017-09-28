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


def setup_system_and_start_servers():
    mcos_celery_server_proc_id = \
        sub_procs_manage.start_handle_cluster_msg_server()
    send_cluster_status_proc_id = \
        sub_procs_manage.start_periodic_send_cluster_status()
    check_cluster_status_proc_id = \
        sub_procs_manage.start_periodic_check__clusters_status()
    print mcos_celery_server_proc_id
    print send_cluster_status_proc_id
    print check_cluster_status_proc_id
    import atexit
    atexit.register(kill_child, [
        mcos_celery_server_proc_id,
        send_cluster_status_proc_id,
        check_cluster_status_proc_id
    ])


def kill_child(sub_procs):
    for sub_proc_id in sub_procs:
        os.kill(sub_proc_id, signal.SIGTERM)
    print("done")


if __name__ == "__main__":
    setup_system_and_start_servers()
    while True:
        print("main_proc")
        time.sleep(5)
