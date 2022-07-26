from django.contrib import admin
from .models import userInfo

# Register your models here.

class userAdmin(admin.ModelAdmin):
    list_display=['firstname','lastname','email','dob','mobile']

admin.site.register(userInfo,userAdmin)