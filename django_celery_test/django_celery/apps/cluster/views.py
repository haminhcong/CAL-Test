from __future__ import absolute_import, unicode_literals
# Create your views here.
import django
import json
import requests
import time
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import SystemCluster


def get_cluster_list(request):
    if request.method == 'GET':
        cluster_list = []
        cluster_data_list = SystemCluster.objects.all()
        for cluster_info in cluster_data_list:
            cluster_list.append(cluster_info.to_dict())
        return JsonResponse({'cluster_list': cluster_list})
