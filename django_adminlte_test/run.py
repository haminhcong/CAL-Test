"""
WSGI config for mcos project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""
import eventlet

eventlet.monkey_patch()

from eventlet import wsgi
from optparse import OptionParser
from os.path import abspath, dirname
from sys import path
import os
from django_adminlte_test.settings import PORT as APP_PORT
from django.core.wsgi import get_wsgi_application

# from all_ring import RingDict

SITE_ROOT = dirname(dirname(abspath(__file__)))
# path.append(SITE_ROOT)
path.insert(0, SITE_ROOT)

MAX_GREEN_THREADS = 25
# RINGS = RingDict()

SYSTEM_INFO = {
    # id of cluster which is holding connect_to_system lock
    'cts_lock_cluster_id': 'none',
    # id of current cluster is running
    'current_cluster_id': 'none',
    # check if user dash board is enabled or not
    'enable_user_dashboard': False

}


def run_wsgi_app(app, port):
    """Run a wsgi compatible app using eventlet"""
    print "starting eventlet server on port %i" % port
    wsgi.server(
        eventlet.listen(('', port)),
        app,
        max_size=25,
    )


def setup_system_and_start_server():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                          "django_adminlte_test.settings")
    application = get_wsgi_application()
    run_wsgi_app(application, int(APP_PORT))


if __name__ == "__main__":
    setup_system_and_start_server()
