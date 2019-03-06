from django.shortcuts import render

def index(request):
    return render(request, 'conveyancing/conveyancing_index.html')
