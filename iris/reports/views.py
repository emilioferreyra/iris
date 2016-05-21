from django.http import HttpResponse
from django.db.models import Count
from django.shortcuts import render


from members.models import Member


def members_by_academic_level(request):
    field = 'academic_level__name'
    queryset = Member.objects.all().\
        values(field).\
        annotate(total=Count(field)).order_by('-total')
    context = {
        "title": "Members Quantity by Academic Level",
        "object_list": queryset
    }
    return render(request, "reports/index.html", context)
