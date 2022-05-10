from importlib import import_module
from django.contrib import admin
from BlogApp.models import Post, Comments
# Register your models here.

admin.site.register(Post)
admin.site.register(Comments)
