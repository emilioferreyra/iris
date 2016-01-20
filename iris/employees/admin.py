from django.contrib import admin

from .models import Employee
from people.admin import PersonAdmin


class EmployeeAdmin(PersonAdmin):
    fields = (
        ('picture', 'names', 'father_last_name', 'mother_last_name', 'email'),
        ('birth_day', 'nationality', 'marital_status'),
        ('gender', 'document_type', 'document_id'),
        'status'
        )

    list_display = [
        'id',
        'picture',
        'full_name',
        'email',
        'calculate_age',
        'birth_day',
        'status'
        ]

    list_filter = [
        'status',
        'marital_status',
        'gender'
    ]

    def get_queryset(self, request):
        qs = super(EmployeeAdmin, self).get_queryset(request)
        return qs.filter(person_type="E")


admin.site.register(Employee, EmployeeAdmin)
