from django.shortcuts import render
from . import models
from .forms import QuoteForm
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from . import forms

class TeacherCreate(CreateView):
    model = models.Teacher
    fields = ['name']
    success_url = reverse_lazy('new_teacher')
    

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

    if not request.session.get('logedin', False):
        return render(request, 'quotes/not_logged_in.html', context={'teachers': teachers, 'new_quote': form, 'likes': likes, 'session_likes': request.session.get('liked', [])})
        
    return render(request, 'quotes/index.html', context={'teachers': teachers, 'new_quote': form, 'likes': likes, 'session_likes': request.session.get('liked', [])})


def likes(request):
    likes = {}
    for quote in models.Quote.objects.all():
        likes[quote.id] = quote.likes

    return JsonResponse(likes)


def like(request, quote_id):
    quote = models.Quote.objects.get(id=quote_id)
    
    liked = [] if not 'liked' in request.session else request.session['liked']
    print(liked)
    if quote_id in liked:
        quote.likes -= 1
        quote.save()
        liked.remove(quote.id)
        request.session['liked'] = liked
        liked = False

    else:
        quote.likes += 1
        quote.save()
        liked.append(quote.id)
        request.session['liked'] = liked
        liked = True

    index = list(quote.teacher.quotes.all()).index(quote)

    return JsonResponse({'id': quote.id, 'likes': quote.likes, 'index': index, 'liked': liked})

def login(request):
    if request.session.get('logedin', False):
        return HttpResponse('1')
    
    if request.POST:
        if request.POST['password'] == 'relpek':
            request.session['logedin'] = True
            return HttpResponse('1')

    return HttpResponse('0')