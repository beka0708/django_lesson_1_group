from django.shortcuts import render
from django.http import HttpResponse
from . import models


def hello_world_view(request):
    return HttpResponse(
        "<body bgcolor=aqua> <h1> My name is Bektur <h2/></body>"
    )


# post_view
def post_view(request):
    post = models.Post.objects.all()
    return render(request, 'index.html', {'post': post})
