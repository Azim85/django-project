from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    # include default auth urlsself.
    path('', include('django.contrib.auth.urls')),
    # registration pageself.
    path('register/', views.register, name='register')
]