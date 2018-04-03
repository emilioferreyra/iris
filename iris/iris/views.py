# -*- coding: utf-8 -*-

# Django modules
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _

# Third-party modules
from suit_dashboard.views import DashboardView
from suit_dashboard.layout import Grid, Row, Column


class HomeView(DashboardView):
    template_name = 'suit_dashboard/template.html'
    crumbs = ({'url': 'admin:index', 'name': _('Home')},)
    grid = Grid(
        Row(Column()),  # default width=12 (maximum)
        Row(Column(width=6), Column(width=1), Column(width=4)),
        Row(Column(  # nested rows and columns
            Row(Column(width=10), Column(width=2)),
            Row(Column(width=4), Column(width=6)), width=5),Column(width=6)
        )
    )


class NestView1(HomeView):
    crumbs = ({'url': 'admin:nest1', 'name': _('Nest 1')},)


class NestView2(NestView1):
    crumbs = ({'url': 'admin:nest2', 'name': _('Nest 2')},)


# def home(request):
#     title = "Iris"
#     project_name = "Iris ACICIRD"
#     greating = "Bienvenidos a Iris!"
#     jumbotron_content = "Iris fue diseñado para ayudar a la correcta\
#         identificación de las necesidades para canalizar los recursos\
#         a los miembros de la Asociación de Ciegos del Cibao \
#         (ACICIRD)."
#     context = {
#         'title': title,
#         'project_name': project_name,
#         'greating': greating,
#         'jumbotron_content': jumbotron_content
#     }
#     return render(request, "home/index.html", context=context)
