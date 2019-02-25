from django.shortcuts import render

def index(request):

    return render(request, 'projek/proj_index.html')
