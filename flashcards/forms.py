from django import forms
from .models import *

class NewCardForms(forms.ModelForm):
    class Meta:
        model = Cards
        fields = ['question', 'answer', 'level']

class FlashcardFilterForm(forms.Form):
    LEVEL_CHOICES = (
        (1, 'Level 1'),
        (2, 'Level 2'),
        (3, 'Level 3'),
    )
    level = forms.ChoiceField(choices=LEVEL_CHOICES, label='Nível')
