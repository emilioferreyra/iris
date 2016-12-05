# -*- coding: utf-8 -*-

from django.db.models import Count
# from django.db.models import Q
from django.shortcuts import render

from members.models import Member
from people.models import PersonAddress


def members_by_academic_level(request):
    field = 'academic_level__name'
    queryset = Member.objects.all().\
        values(field).\
        annotate(total=Count(field)).\
        order_by('-total')
    context = {
        "title": "Miembros por Nivel Académico",
        "object_list": queryset
    }
    # return render(request, "reports/index.html", context)
    return render(request, "reports/members_by_academic_level.html", context)


# Variables declaration
person_type_member = 2
address_type_home = 1


def members_by_location(request):
    field = 'location__name'
    queryset = PersonAddress.objects.filter(
        person_name__person_type_id=person_type_member,
        address_type_id=address_type_home).\
        exclude(location__isnull=True).values(field).\
        annotate(total=Count(field)).\
        order_by("-total")
    context = {
        "title": "Miembros por Localidad",
        "object_list": queryset
    }
    return render(request, "reports/member_by_location.html", context)


def mothers_quantity(request):
    field = 'marital_status__name'
    queryset = Member.objects.filter(is_mother=True). \
        values(field). \
        annotate(total=Count(field)). \
        order_by('-total')
    total_mothers = Member.objects.filter(is_mother=True).count()
    context = {
        "title": "Miembros Madres",
        "object_list": queryset,
        "total_mothers": total_mothers
    }
    return render(request, "reports/mothers.html", context)
