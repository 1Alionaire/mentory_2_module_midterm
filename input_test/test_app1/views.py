from django.shortcuts import render, HttpResponseRedirect
from test_app1.forms import InputFeedback
from django.urls import reverse
from datetime import datetime
from test_app1.models import Animals

def index(request):
    context = {'title': 'Главная',
               'animals': Animals.objects.all()
               }
    return render(request, 'test_app1/index.html', context)

def index_form(request):
    if request.method == 'POST':
        form = InputFeedback(request.POST)
        if form.is_valid():
            kek = form.save(commit=False)
            kek.input_time = datetime.now()
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = InputFeedback()
    context = {'form':form, 'title':'Фидбэчная'}
    return render(request, 'test_app1/input_form.html', context)
