# """Определяет схемы URL для learning_logs."""
from django.urls import path as url
from . import views
urlpatterns = [
    # Home page.
    url('', views.index, name='index'),

    # Show all topics.
    url('topics/', views.topics, name='topics'),

    # Detail page for a single topic.
    url('topics/<topic_id>/', views.topic, name='topic'),

    # Page for adding a new topic.
    url('new_topic/', views.new_topic, name='new_topic'),

    # Page for adding a new entry.
    url('new_entry/<topic_id>/', views.new_entry, name='new_entry'),

    # Page for editing an entry.
    url('edit_entry/<entry_id>/', views.edit_entry,
        name='edit_entry'),
]
