from django.shortcuts import render
from .models import PageIntro
# Create your views here.


def index(request):
    page_intros = PageIntro.objects.all()
    template = 'home/index.html'
    context = {
        'page_intros': page_intros,
    }
    return render(request, template, context)
