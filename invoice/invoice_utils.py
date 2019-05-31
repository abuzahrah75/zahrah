from .models import *

def get_active_invoice():
    retdata = InvoiceParticular.objects.filter(status='OP')
    return retdata