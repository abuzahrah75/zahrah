from django.contrib import admin
from .models import ClientFolder


class ClientFolderAdmin(admin.ModelAdmin):
    list_display=('rujukan','nama','kategori','kat_pelanggan')
    #list_display = ('rujukan', 'nama', 'kat_pelanggan')
    search_fields =('rujukan','nama')


admin.site.register(ClientFolder, ClientFolderAdmin)
