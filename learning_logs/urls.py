#"""Определяет схемы URL для learning_logs."""
from django.urls import path as url
from . import views
urlpatterns = [
# Домашняя страница
       url('', views.index, name='index'),
       # Вывод всех тем.
       url(r'topics/', views.topics, name='topics'),
       # Вывод всех тем.
       url('<topic_id>/', views.topic, name='topic'),
       url(r'new_topic/$', views.new_topic, name='new_topic'),
       url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
# Страница для редактирования записи
       url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,
    name='edit_entry'),

]