from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='default_index'),
    url(r'^news', views.index, name='index'),
    url(r'^chart', views.chart, name='chart'),
]
