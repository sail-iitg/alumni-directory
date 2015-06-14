from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect

def home(request):
    """Homepage for website"""
    return render_to_response('sail/home.html')
