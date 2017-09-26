from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

import views

urls = [

    url(r'^$',
        views.dashboard, name='dashboard'),
    url(r'^info', views.dashboard_info, name='dashboard_info')
]
urlpatterns = urls
# urlpatterns = urls + static(settings.MEDIA_URL,
#                             document_root=settings.MEDIA_ROOT)
