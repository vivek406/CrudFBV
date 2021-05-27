from django.contrib import admin

# Register your models here.
from crudFBVapp.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddr']

admin.site.register(Employee,EmployeeAdmin)
