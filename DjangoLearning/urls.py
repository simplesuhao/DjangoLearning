from django.conf.urls import url
from django.contrib import admin

from new_test import add
from new_test import helloworld
from new_test import list
urlpatterns = [
    url(r'^list/$', list.index),
    url(r'^$', helloworld.index),
    url(r'^add/$', add.index),
    url(r'^admin/', admin.site.urls),
]

