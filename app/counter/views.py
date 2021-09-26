from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import CounterModel

def about(request):
    return HttpResponse("<h3> Hello from Olimpiev!</h3>")

def index(request):
    obj = CounterModel.objects.first()
    context = {'number': obj.number}
    return render(request, 'base.html', context)

def stat(request):
    obj = CounterModel.objects.first()
    obj.number = int(obj.number) + 1
    obj.save()
    context = {'number': obj.number}
    return render(request, 'base.html', context)
