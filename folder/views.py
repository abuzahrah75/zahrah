from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *

def index(request):
    return render(request, 'folder/folder_index.html')


def folder_create(request):
    pk=1
    if request.method == 'POST':
        #name = 'testing'
        form = ClientFolderForm(request.POST)
        if form.is_valid():
            form.save()
            reurl = '/contacts/mycontact/update/' + str(pk)
            return HttpResponseRedirect(reurl)
    else:
        form = ClientFolderForm()
    return render(request, 'folder/clientfolder_form.html', {
        'form': form,
        'pk': pk,
    })
