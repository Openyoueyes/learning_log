from django.urls import include
from django.urls import path as url
from django.contrib import admin
#"""Определяет схемы URL для learning_logs."""
from learning_logs import views
urlpatterns = [
    url('admin/', admin.site.urls),
    url('users/', include(('users.urls', 'users'), namespace='users')),
    url('', include(('learning_logs.urls','learning_logs'), namespace='learning_logs')),
]
