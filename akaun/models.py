from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from home.models import Cawangan


class AkaunBank (models.Model):
    JENIS_AKAUN = (
        ('CLIENT', 'CLIENT ACCOUNT'), 
        ('OFFICE', 'OFFICE ACCOUNT'),
        ('OTHER','OTHER ACCOUNT')
    )
    nama = models.CharField(max_length=120, default='')
    jenis = models.CharField(max_length=10, default='', choices=JENIS_AKAUN)
    no_akaun = models.CharField(max_length=20, default='')
    bank = models.CharField(max_length=120, default='')
    cawangan_bank = models.CharField(max_length=120, default='')
    cawangan = models.ForeignKey(Cawangan, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural='Akaun Bank'
    
    def __str__(self):
        return self.nama + ' ('+ self.no_akaun + ') - ' + self.jenis

class KategoriTransaksi(MPTTModel):
    nama = models.CharField(max_length=200, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True,
                            blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['nama']

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = 'Kategori Transaksi'
       


class RightsSupport(models.Model):

    class Meta:

        managed = False  # No database table creation or deletion  \
        # operations will be performed for this model.

        permissions = (
            ('level1', 'Level 1 Permission'),
            ('level2', 'Level 2 Permission'),
            ('level3', 'Level 3 Permission'),
            ('level4', 'Level 4 Permission'),
            ('level5', 'Level 5 Permission'),
            ('level6', 'Level 6 Permission'),
            ('level7', 'Level 7 Permission'),
        )
