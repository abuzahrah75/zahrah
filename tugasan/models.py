from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from folder.models import ClientFolder


class KategoriTugasan(MPTTModel):
    nama = models.CharField(max_length=200, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True,
                            blank=True, related_name='children')
    class Meta:
        verbose_name_plural = 'Kategori Tugasan'
        
    class MPTTMeta:
        order_insertion_by = ['nama']

    def __str__(self):
        return self.nama


class TugasanTemplate(models.Model):
    pass


class TugasanConfig(models.Model):
    pass


class MyTugasan(models.Model):
    STATUS_LIST = (
        ('FN', 'FINISHED'), ('PD', 'PENDING'),
        ('OP', 'ON PROGRESS'), ('CA', 'CANCEL'),
        ('HT','HALTED'),('NA', 'NOT APLICABLE'),('ST','STARTED')
    )
    nama = models.CharField(max_length=200, unique=True, default='')
    folder = models.ForeignKey(
        ClientFolder, on_delete=models.CASCADE, null=True, blank=True)
    kategori_tugasan = TreeForeignKey(
        KategoriTugasan, on_delete=models.CASCADE, null=True, blank=True)
    status_tugasan = models.CharField(
        max_length=2, default='ST', choices=STATUS_LIST)


    def __str__(self):
        return self.nama
