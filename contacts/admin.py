from django.contrib import admin
from .models import Warganegara, MyContacts, ContactCategory, ContactEmail, ContactPhone, ContactAddress

admin.site.register(Warganegara)
admin.site.register(MyContacts)
admin.site.register(ContactCategory)
admin.site.register(ContactEmail)
admin.site.register(ContactPhone)
admin.site.register(ContactAddress)
