from django.shortcuts import render
import datetime


def home(request):
    data = datetime.datetime.now().date()
    name = 'Max'
    context = {'data': data, 'name': name}
    return render(request, 'home.html', context)
