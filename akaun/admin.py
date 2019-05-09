from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import AkaunBank, KategoriTransaksi


class AkaunBankAdmin(admin.ModelAdmin):
    list_display = ('nama', 'jenis', 'no_akaun', 'bank', 'cawangan_bank', 'cawangan')
    #list_display = ('rujukan', 'nama', 'kat_pelanggan')
    #search_fields = ('rujukan', 'nama')


admin.site.register(
    KategoriTransaksi,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
        'level',
        'id', 'lft', 'rght'

    ),
    list_display_links=(
        'indented_title',
    ),
)

admin.site.register(AkaunBank, AkaunBankAdmin)
