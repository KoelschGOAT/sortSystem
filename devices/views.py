from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.template import Context, loader
#Create your views here.
def index(request):
    return render(request, 'index.html')
