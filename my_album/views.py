from django.http import request
from django.shortcuts import render

from .models import myAlbum

# Create your views here.
def my_album(request):
      
      album = myAlbum.objects.all()

      context = {
            'album' : album
      }

      return render(request, 'album/index.html', context)