from django.urls import include
from django.urls import path as url
from django.contrib import admin
#"""Определяет схемы URL для learning_logs."""
from learning_logs import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include(('learning_logs.urls','learning_logs'), namespace='learning_logs')),
# Домашняя страница
    url('', views.index, name='index'),
]
#url(r'^reviews/', include(('reviews.urls', 'reviews'), namespace='reviews')),