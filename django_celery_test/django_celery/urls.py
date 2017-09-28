from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include, url


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
                  url(r'^',
                      include('django_celery.apps.cluster.urls',
                              namespace='cluster')),
              ] + staticfiles_urlpatterns()

# urlpatterns = patterns(
#     url(r'^$', 'django_celery.apps.cluster.views.home', name='home'),
    # Examples:
    # url(r'^$', 'proj.views.home', name='home'),
    # url(r'^proj/', include('proj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
# )
