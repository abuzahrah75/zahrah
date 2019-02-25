from django.shortcuts import render
from django.http import HttpResponse
from tenants.utils import tenant_from_request

def index(request):

    #return HttpResponse(str(tenant_from_request(request)))
    return HttpResponse(str(request.get_host()))
