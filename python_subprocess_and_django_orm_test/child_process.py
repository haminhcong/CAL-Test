import os
import time
import django


def setup_django_db_context(db_setting_modules):
    os.environ['DJANGO_SETTINGS_MODULE'] = db_setting_modules
    django.setup()


setup_django_db_context(db_setting_modules='mcos_settings')
from models import SystemCluster, ObjectServiceInfo

with open("test.txt", "a") as test_text_file:
    while True:
        for cluster in SystemCluster.objects.all():
            test_text_file.write(cluster.name + "\n")
        test_text_file.write("\n\n")
        time.sleep(3)
