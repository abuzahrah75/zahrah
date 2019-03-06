from django.shortcuts import render

def index(request):
    return render(request, 'folder/folder_index.html')
