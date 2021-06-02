from django.contrib import admin

# Register your models here.
from .models import myAlbum

class MyAlbumAdmin(admin.ModelAdmin):
      list_display = [
            'description',
            'thumbnail',
            'creation'
      ]

#regirster
admin.site.register(myAlbum, MyAlbumAdmin)