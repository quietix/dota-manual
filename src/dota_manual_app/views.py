from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Build
from django.http import FileResponse

def send_file(response):
    img = open('media/images/juggernaut.png', 'rb')
    response = FileResponse(img)
    return response


class HomePageView(ListView):
    model = Build
    template_name = "home.html"


