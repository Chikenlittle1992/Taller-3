from django.shortcuts import render
from .models import Shows

# Create your views here.
def news(request):
    shows = Shows.objects.all().order_by('-puntuation')
    return render(request, 'shows.html', {'shows':shows})
