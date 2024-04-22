from django.shortcuts import render
from .models import *

def index(request):
    queryset = Cards.objects.all()
    levels = range(1,6)
    context = {'flashcards': queryset, 'levels':levels}


    return render(request, 'index.html', context = context)