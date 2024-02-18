from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Build


class HomePageView(ListView):
    model = Build
    template_name = "home.html"
