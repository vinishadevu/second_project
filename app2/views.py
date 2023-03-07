from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse



def first_app2(request):
    return HttpResponse('<h2>FIRST VIEW FUNCTION OF APP2</h2>')