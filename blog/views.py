from django.shortcuts import render
from django.http import HttpResponse


def hello_world_view(request):
    return HttpResponse(
        "<body bgcolor=aqua> <h1> My name is Bektur <h2/></body>"
    )
