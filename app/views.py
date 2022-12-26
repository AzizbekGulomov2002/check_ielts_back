
from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.

from .models import IELTS


class IELTSViews(ListView):
    model = IELTS
    context_object_name = 'ielts'
    template_name = 'blog/index.html'
    
    
class MainViews(ListView):
    model = IELTS
    context_object_name = 'ielts'
    template_name = 'blog/index2.html'




