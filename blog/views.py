from pdb import post_mortem
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DeleteView
from .models import logbook

def home(request):
    return render(request, 'blog/home.html')

def appointment(request):
    return render(request, 'blog/appointment.html')

def grade(request):
    return render(request, 'blog/grade.html')

#def logbook(request):
#    return render(request, 'blog/logbook.html')

def lprofile(request):
    return render(request, 'blog/lprofile.html')

def lprofile1(request):
    return render(request, 'blog/lecturer1.html')

def lprofile2(request):
    return render(request, 'blog/lecturer2.html')

def notification(request):
    return render(request, 'blog/notification.html')

def schedule(request):
    return render(request, 'blog/schedule.html')

def sprofile(request):
    return render(request, 'blog/sprofile.html')

def studentc(request):
    return render(request, 'blog/studentc.html')

def studentd(request):
    return render(request, 'blog/studentd.html')

def progression(request):
    return render(request, 'blog/progression.html')

class logbookView(ListView):
    model = logbook
    template_name = 'blog/logbook.html'

class AddlogbookView(CreateView):
    model = logbook
    template_name = 'blog/addlogbook.html'
    fields = '__all__'