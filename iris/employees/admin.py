from django.contrib import admin

from .models import Employee
from people.admin import PersonAdmin


class EmployeeAdmin(PersonAdmin):
    fields = (
        ('names', 'father_name', 'mother_name', 'email'),
        ('birth_day', 'nationality', 'marital_status'),
        ('gender', 'document_type', 'document_id'),
        ('dependent', 'parent_of'),
        'status'
        )

    list_filter = ['status']

    def get_queryset(self, request):
        qs = super(EmployeeAdmin, self).get_queryset(request)
        return qs.filter(person_type="E")


admin.site.register(Employee, EmployeeAdmin)
