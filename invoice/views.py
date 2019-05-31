from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse
from .invoice_utils import *


def index(request):
    return render(request, 'invoice/invoice_index.html')

def invoice_list(request):
    context = {
        'senarai': get_active_invoice()
    }

    return render(request, 'invoice/inv_list.html', context)

def invoice_detail(request, pk):
    context={}

    return render(request, 'invoice/inv_detail.html', context)
