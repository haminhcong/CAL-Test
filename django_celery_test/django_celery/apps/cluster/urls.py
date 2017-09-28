from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

import views

urls = [

    url(r'^$',
        views.get_cluster_list, name='cluster_list'),
]
urlpatterns = urls
# urlpatterns = urls + static(settings.MEDIA_URL,
#                             document_root=settings.MEDIA_ROOT)
