from django.urls import path, include
from . import views

app_name = 'Profile_001'

urlpatterns = [
    path('', views.homepage, name='homepage')
]
