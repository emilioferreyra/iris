from django.contrib import admin

from . import models
from people.admin import PersonAdmin


class MemberAdmin(PersonAdmin):
    fields = (
        ('names', 'father_name', 'mother_name', 'email'),
        ('birth_day', 'nationality', 'marital_status'),
        ('gender', 'document_type', 'document_id'),
        ('dependent', 'parent_of'),
        'status'
        )

    list_filter = ['status']

    def get_queryset(self, request):
        qs = super(MemberAdmin, self).get_queryset(request)
        return qs.filter(person_type="M")


admin.site.register(models.Disability)
admin.site.register(models.Cane)
admin.site.register(models.Member, MemberAdmin)
admin.site.register(models.Housing)
