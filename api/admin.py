from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Company)
admin.site.register(Department)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "position")
    search_fields = ("first_name",)
    list_filter = ("company_detail",) # filter employee by company wise
admin.site.register(Employee, EmployeeAdmin)
