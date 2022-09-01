from django.contrib import admin

from .models import Contact, CustomUser
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Contact)
