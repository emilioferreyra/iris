# -*- coding: utf-8 -*-

from django.shortcuts import render


def home(request):
    title = "Iris"
    project_name = "Iris ACICIRD"
    greating = "Bienvenidos a Iris!"
    jumbotron_content = "Iris fue diseñado para ayudar a la correcta\
        identificación de las necesidades para canalizar los recursos\
        a los miembros de la Asociación de Ciegos del Cibao \
        (ACICIRD)."
    context = {
        'title': title,
        'project_name': project_name,
        'greating': greating,
        'jumbotron_content': jumbotron_content
    }
    return render(request, "home/index.html", context=context)
