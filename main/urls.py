from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.news, name='news'),
    path('topic/<int:topic_id>', views.current_topic, name='current_topic'),
    path('new_topic/', views.new_topic, name="new_topic"),
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>', views.edit_entry, name="edit_entry"),
]