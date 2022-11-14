from django.contrib import admin
from .models import User, Book, ReadingStatus
# Register your models here.

admin.site.register(User)
admin.site.register(Book)
admin.site.register(ReadingStatus)
