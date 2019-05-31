from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import KategoriTugasan, MyTugasan

admin.site.register(
    KategoriTugasan,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
        'level', 'id', 'lft', 'rght'

    ),
    list_display_links=(
        'indented_title',
    ),
)

admin.site.register(MyTugasan)
