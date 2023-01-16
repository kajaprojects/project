from django.contrib import admin
from .models import Post, Comment, Image

admin.site.register(Post)
admin.site.register(Comment)

class imageAdmin(admin.ModelAdmin):
    list_display = ["title", "photo"]

admin.site.register(Image, imageAdmin)