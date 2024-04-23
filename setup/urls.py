from django.contrib import admin
from django.urls import path
from flashcards.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    path('delete/<int:card_id>', delete, name = 'delete'),
    path('new/', new, name = 'new'),
    path('study_mode/', study_mode, name = 'study_mode'),
]
