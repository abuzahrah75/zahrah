from django.contrib import admin
from .models import Conveyancing, JenisHartanah


class ConveyancingAdmin(admin.ModelAdmin):
    list_display = ('ringkas', 'pembeli', 'penjual')
    search_fields = ('ringkas', 'pembeli')


admin.site.register(Conveyancing, ConveyancingAdmin)
admin.site.register(JenisHartanah)
