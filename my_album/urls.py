from django.urls import path, include
from . import views

app_name = 'my_album'

urlpatterns = [
    path('', views.my_album, name='my_album')
]
