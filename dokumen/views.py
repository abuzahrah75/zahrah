from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from folder.models import ClientFolder
from .forms import DocumentForm
from .models import Document


def index(request):

    mydocument = Document.objects.all().order_by('-uploaded_at')
    context={
        'mydoc': mydocument
    }
    return render(request, 'dokumen/dokumen_index.html', context)


def testmerger(request):
    from mailmerge import MailMerge
    from datetime import date
    #get merger document
    dokumen=Document.objects.get(pk=5)
    # get the data for merger from ClientFolder
    pelanggan = ClientFolder.objects.get(id=1)

    from mailmerge import MailMerge
    from datetime import date

    #template = "media/test-merger.docx"
    document = MailMerge(dokumen.document.path)
    senarai = document.get_merge_fields()

    document.merge(nama=pelanggan.nama, rujukan=pelanggan.rujukan, kategori=pelanggan.get_kategori_display())
    namafail = 'media/azmi/testmerger_' + pelanggan.nama + '_' + str(date.today()) +'.docx' 
    document.write(namafail)
    #return render(request, 'home/testmerger.html', context)

    return HttpResponseRedirect('/'+namafail)


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


def testupload2(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dokumen')
    else:
        form = DocumentForm()
        return render(request, 'dokumen/model_form_upload.html', {
        'form': form
    })


def mergemydoc(request,docid=0,dataid=0):


    return HttpResponse("temporary response.")