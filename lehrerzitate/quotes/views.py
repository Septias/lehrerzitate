from django.shortcuts import render
from . import models
from .forms import QuoteForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


class TeacherCreate(CreateView):
    model = models.Teacher
    fields = ['name']
    success_url = reverse_lazy('index')

def index(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse_lazy('index'))

    form = QuoteForm()
    teachers = filter(lambda x: len(x.quotes.all()) > 0, models.Teacher.objects.all())
    return render(request, 'quotes/index.html', context={'teachers': teachers, 'new_quote': form})