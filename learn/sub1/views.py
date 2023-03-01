from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def main(request):
    return HttpResponse("VITEK PESSSS")

def categs(request, id: int = 0):
    d = request.GET
    # s = f'Categs {id=}'
    # if d:
    f = ' '.join(map(str, d.items()))
    s = f'Categs {id=}, params {f if f else "are empty"}'
    return HttpResponse(s)