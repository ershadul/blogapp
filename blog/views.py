from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def all_posts(request):
    return HttpResponse('Hi, Welcome!')