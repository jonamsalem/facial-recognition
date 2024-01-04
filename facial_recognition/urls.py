# project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('facial_recognition_app.urls')),  # Replace 'myapp' with your app's name
]
