# path needed to map urls to views
from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    #Homepage
    path('', views.index, name='index'),

    # Topics
    path('topics/', views.topics, name='topics'),

    # Single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # Add topic
    path('new_topic/', views.new_topic, name='new_topic'),

    # Add entry
    path('new_entry/<int:topic_id>/',views.new_entry, name='new_entry'),
]