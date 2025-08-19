from django.contrib import admin
from .models import CustomUser, Category, MusicSheet, DownloadLog

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(MusicSheet)
admin.site.register(DownloadLog)
