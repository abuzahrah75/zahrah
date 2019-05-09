from django.contrib import admin
#from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin
from .models import Kategori, Cawangan

#admin.site.register(Kategori, MPTTModelAdmin)
admin.site.register(
    Kategori,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
        'level',
        'id', 'lft','rght'
        
    ),
    list_display_links=(
        'indented_title',
    ),
)

admin.site.register(Cawangan)