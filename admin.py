from .models import Comment,Conect
from django.contrib import admin

from app.models import Blog

# Register your models here.
admin.site.register(Blog)
admin.site.register(Conect)
admin.site.register(Comment)