from django.contrib import admin

# Register your models here.
from rabc import models

class PerConfig(admin.ModelAdmin):
    list_display = ['title','url','group','action']


admin.site.register(models.User)
admin.site.register(models.Role)
admin.site.register(models.Permission,PerConfig)
admin.site.register(models.PermissonGroup)





