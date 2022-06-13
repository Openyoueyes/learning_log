# """Определяет схемы URL для learning_logs."""
from django.urls import path as url
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    # Страница входа
    url('login/', LoginView.as_view(template_name='users/login.html'), name="login"),
    # Страница выхода
    url('logout/', views.logout_view, name='logout'),
    # страница регистрации
    url('register/', views.register, name='register')
]
