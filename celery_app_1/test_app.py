from celery_test import tasks
for x in range(1,5):
    tasks.add.delay(4,5)

