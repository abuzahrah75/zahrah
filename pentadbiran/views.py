from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

def index(request):
    return render(request, 'pentadbiran/pentadbiran_index.html')

