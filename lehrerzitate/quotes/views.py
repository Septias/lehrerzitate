from django.shortcuts import render
from . import models
from .forms import QuoteForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from . import forms

class TeacherCreate(CreateView):
    model = models.Teacher
    fields = ['name']
    success_url = reverse_lazy('index')


def report(request, quote_id):
    quote = models.Quote.objects.get(id=quote_id)

    if request.method == 'POST':
        form = forms.ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('index'))
    
    elif request.method == 'GET':
        form = forms.ReportForm(initial={'quote': quote})
    
    return render(request, 'quotes/report_form.html', context={'form': form})
    

def index(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('index'))

    else:
        form = QuoteForm()
        
    teachers = filter(lambda x: len(x.quotes.all()) > 0, models.Teacher.objects.all())
    return render(request, 'quotes/index.html', context={'teachers': teachers, 'new_quote': form})