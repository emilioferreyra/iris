from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple

from .models import Member, MemberAdditionalField, Disability, Cane, Housing
from people.admin import \
    PersonAdmin, PersonAddressInlines, PersonPhoneInlines, KinsmanInline


class MemberAdditionalFieldInline(admin.StackedInline):
    model = MemberAdditionalField
    min_num = 1
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


class HousingInline(admin.TabularInline):
    model = Housing
    min_num = 3
    max_num = 3
    extra = 0


class MemberAdmin(PersonAdmin):
    fields = (
        ('names', 'father_last_name', 'mother_last_name', 'email'),
        ('birth_day', 'nationality', 'marital_status'),
        ('gender', 'document_type', 'document_id'),
        # ('dependent', 'parent_of'),
        'status'
        )

    # list_display = [
    #     'id',
    #     'full_name',
    #     'email',
    #     'status'
    #     ]

    list_filter = ['status']

    inlines = [
        PersonAddressInlines,
        PersonPhoneInlines,
        MemberAdditionalFieldInline,
        KinsmanInline,
        HousingInline
    ]

    def get_queryset(self, request):
        qs = super(MemberAdmin, self).get_queryset(request)
        return qs.filter(person_type="M")


admin.site.register(Disability)
admin.site.register(Cane)
admin.site.register(Member, MemberAdmin)
admin.site.register(Housing)
