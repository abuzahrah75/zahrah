from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from folder.folder_utils import get_folder

def index(request):
    context = {'myfolder': get_folder(request), }
    #return HttpResponse(context)
    return render(request, 'pelanggan/pelanggan_index.html',context)
