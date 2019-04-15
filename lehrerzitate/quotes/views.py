from django.shortcuts import render
from . import models
from .forms import QuoteForm
from django.http import HttpResponseRedirect, JsonResponse
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

    likes = {}
    for quote in models.Quote.objects.all():
        likes[quote.id] = quote.likes

    teachers = filter(lambda x: len(x.quotes.all().order_by('likes')) > 0, models.Teacher.objects.all())
    return render(request, 'quotes/index.html', context={'teachers': teachers, 'new_quote': form, 'likes': likes, 'session_likes': request.session.get('liked', [])})


def likes(request):
    likes = {}
    for quote in models.Quote.objects.all():
        likes[quote.id] = quote.likes

    return JsonResponse(likes)


def like(request, quote_id):
    quote = models.Quote.objects.get(id=quote_id)
    try:
        if quote_id not in request.session.get('liked'):
            quote.likes += 1
            quote.save()
            request.session['liked'] += [quote.id]
        
    except TypeError:
        request.session['liked'] = list()
        quote.likes += 1
        quote.save()
        request.session['liked'].append(quote_id)

    index = tuple(models.Quote.objects.all()).index(quote)
    if index == 1:
        index = 0
        
    return JsonResponse({'id': quote.id, 'likes': quote.likes, 'index': index})
