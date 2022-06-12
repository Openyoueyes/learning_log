#"""Определяет схемы URL для learning_logs."""
from django.urls import path as url
from . import views
urlpatterns = [
# Домашняя страница
       url('', views.index, name='index'),
       # Вывод всех тем.
       url(r'^topics/$', views.topics, name='topics'),
       # Вывод всех тем.
       url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

]