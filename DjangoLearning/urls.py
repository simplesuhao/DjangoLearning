from django.conf.urls import url
from django.contrib import admin

from new_test import add
from new_test import csv_test
from new_test import helloworld
from new_test import list
urlpatterns = [
    url(r'^csv/(?P<filename>\w+)/$', csv_test.output),
    url(r'^list/$', list.index),
    url(r'^$', helloworld.index),
    url(r'^add/$', add.index),
    url(r'^admin/', admin.site.urls),
]

