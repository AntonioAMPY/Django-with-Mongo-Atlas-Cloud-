from django.shortcuts import render
from .models import Personas
from django.http import HttpResponse


def index(request):
    s = Personas.objects.all()
    
    return render(request, 'index.html', {'s': s})