from django.shortcuts import render
from . import models
from .forms import QuoteForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
    
    form = QuoteForm()
    teachers = models.Teacher.objects.all()
    return render(request, 'quotes/index.html', context={'teachers': teachers, 'new_quote': form})