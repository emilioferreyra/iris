from django.contrib import admin

from .models import Doctor
from people.admin import PersonAdmin, PersonPhoneInlines \
    # , PersonAddressInlines


class DoctorAdmin(PersonAdmin):
    fields = (
        ('picture', 'names', 'father_last_name', 'mother_last_name', 'email'),
        ('birth_day', 'nationality', 'marital_status'),
        ('gender', 'document_type', 'document_id'),
        # ('dependent', 'parent_of'),
        'status'
        )

    list_display = [
        'id',
        'person_type',
        'full_name',
        'email'
        ]

    inlines = [
        # PersonAddressInlines,
        PersonPhoneInlines
    ]

    list_filter = ['status']

    def get_queryset(self, request):
        qs = super(DoctorAdmin, self).get_queryset(request)
        return qs.filter(person_type="D")

admin.site.register(Doctor, DoctorAdmin)
