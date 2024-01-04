# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('start-facial-recognition/', views.facial_recognition_view, name='start_facial_recognition'),
]
