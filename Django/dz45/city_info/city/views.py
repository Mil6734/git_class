from django.shortcuts import render
from .models import City


def index(request):
    city = City.objects.all()
    return render(request, 'city/index.html', {'city': city})