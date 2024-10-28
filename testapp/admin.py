from django.contrib import admin
from testapp.models import student

class studentAdmin(admin.ModelAdmin):
    list_display=['name','mark']
admin.site.register(student,studentAdmin)
