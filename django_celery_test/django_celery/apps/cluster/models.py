from __future__ import absolute_import, unicode_literals
# Create your models here.
import json
import uuid
from django.db import models  # noqa
from django.utils import timezone


class SystemCluster(models.Model):
    class Meta:
        db_table = 'system_cluster'
        app_label = 'cluster'

    # uuid
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # cluster name
    name = models.CharField('name', max_length=255, unique=True)
    # cluster address
    address_ip = models.CharField('ip', max_length=255)
    address_port = models.CharField('port', max_length=255)
    last_update = models.DateTimeField('last_update',
                                       default=timezone.localtime)

    def to_dict(self):
        cluster_info_dict = {
            'id': str(self.id),
            'name': self.name,
            'address_ip': self.address_ip,
            'address_port': self.address_port,
            'last_update':str(timezone.localtime(self.last_update))

        }
        return cluster_info_dict
