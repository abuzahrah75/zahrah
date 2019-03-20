from __future__ import print_function
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

def index(request):

    if request.user.is_authenticated:
        return render(request, 'home/homeindex.html')
    else:
        return render(request, 'home/homeindex2.html')

def testmerger(request):

    
    from mailmerge import MailMerge
    from datetime import date

    template = "media/test-merger.docx"
    document = MailMerge(template)
    senarai = document.get_merge_fields()
    
    context = {
        'test': senarai,
    }

    document.merge(nama='Awang Selamat', nokp='777777-21-5821')
    document.write('media/azmi/test-merger.docx')
    return render(request, 'home/testmerger.html', context)
