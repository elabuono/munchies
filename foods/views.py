from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Cuisine

def index(request):
    cuisine_list = Cuisine.objects.all()
    template = loader.get_template('foods/index.html')
    context = {
        'cuisine_list': cuisine_list,
    }
    return HttpResponse(template.render(context, request))
