from django.contrib import admin
from .models import Blog, Author, Entry
# Register your models here.
admin.site.register(Entry)
admin.site.register(Author)
admin.site.register(Blog)