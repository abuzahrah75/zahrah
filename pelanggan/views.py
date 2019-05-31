from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from folder.folder_utils import get_folder, get_client
from contacts.contacts_utils import get_extra_info

def index(request):
    context = {'myfolder': get_folder(request), }
    #return HttpResponse(context)
    return render(request, 'pelanggan/pelanggan_index.html',context)


def details(request, pk):
    context = {
        'myclient': get_client(request, pk), 
        'mymatter': "mau beli rumah lorr",
        'contacts': get_extra_info(request, pk)
        }
    return render(request, 'pelanggan/pelanggan_details.html', context)
