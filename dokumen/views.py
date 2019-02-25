from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

def index(request):
    return render(request, 'dokumen/dokumen_index.html')

