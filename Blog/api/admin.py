from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class Blog(admin.ModelAdmin):
    list_display = ['title','description','image','author_name','author_email','author_phone','created_at']