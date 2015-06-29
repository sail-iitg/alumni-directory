from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from sail.models import AlumnusProfile
from django.db.models import Q

fields = ['roll_number', 'name',  'batch']

def createQuery(request, result, field):
    if request.POST[field] == "1":
        # result = result & Q(field + __contains = request.POST['id_' + field])
        result = result & Q(**{field + "__contains" : request.POST['id_' + field]})
    elif request.POST[field] == "2":
        # result = result & Q(field = request.POST['id_' + field])
        result = result & Q(**{field  : request.POST['id_' + field]})

    return result

def home(request):
    """Homepage for website"""
    if request.method=="POST":
        result = Q()
        for field in fields:
            result = createQuery(request, result, field)

        queryResult = AlumnusProfile.objects.filter(result)
        for item in queryResult:
            print item
    return render(request, 'sail/home.html')
