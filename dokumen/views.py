from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from folder.models import ClientFolder


def index(request):
    return render(request, 'dokumen/dokumen_index.html')


def testmerger(request):
    return HttpResponse("testing")


def testupload(request):
    from django.conf import settings
    from django.core.files.storage import FileSystemStorage
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'dokumen/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'dokumen/simple_upload.html')
