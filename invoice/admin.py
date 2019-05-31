from django.contrib import admin
from .models import InvoiceParticular, InvoiceItem

admin.site.register(InvoiceParticular)
admin.site.register(InvoiceItem)
