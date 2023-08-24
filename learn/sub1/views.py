from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.
menu = [f'item_{i}' for i in range(5)]


def main(request):
    return render(request, 'sub1/index.html', {'menu': menu, 'title': 'Main'})


def categs(request, id: int = 0):
    d = request.GET
    # s = f'Categs {id=}'
    # if d:
    f = ' '.join(map(str, d.items()))
    s = f'Categs {id=}, params {f if f else "are empty"}'
    context = {'users': User.objects.all()}
    return render(request, 'sub1/categs.html', context=context)
