from django.shortcuts import render, redirect
from .models import *
from .forms import * 

def index(request):
    queryset = Cards.objects.all()
    levels = range(1,4)

    filter_form = FlashcardFilterForm(request.GET)

    if filter_form.is_valid() and 'level' in filter_form.cleaned_data:
        level = filter_form.cleaned_data['level']
        queryset = queryset.filter(level=level)
    
    context = {'flashcards': queryset, 'levels':levels, 'filter_form': filter_form}



    return render(request, 'index.html', context = context)

def delete(request, card_id):
    card = Cards.objects.get(id = card_id)
    card.delete()
    return redirect('index')

def new(request):
    if request.method == 'POST':
        form = NewCardForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NewCardForms()
    return render(request, 'create_new.html', {'form': form})

def study_mode(request):
    flashcards = Cards.objects.all().order_by('?')
    context = {'flashcards': flashcards}
    return render(request, 'study_mode.html', context = context)
