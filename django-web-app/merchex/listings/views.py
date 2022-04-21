# ~/Open Classrooms/Projets_DAP/P9_RIO_Olivier/cours/Cours_Django/django-web-app/merchex/listings/views.py

from django.http import HttpResponse
from django.shortcuts import render
from requests import request
from listings.models import Band, Listing

def hello(request):
    bands = Band.objects.all()
    return render(request,
     'listings/hello.html',
     {'bands': bands})

def about(request):
    return render(request, 'listings/about.html')

def listings(request):
    listings = Listing.objects.all()
    return render(request,
     'listings/listings.html',
      {'listings': listings})

def contact(request):
    return render(request, 'listings/contact.html')
