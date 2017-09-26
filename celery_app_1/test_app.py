from celery_test import tasks
for x in range(1,20):
    tasks.add.delay(4,5)

