from django.db import models


class ClientFolder(models.Model):
    KATEGORI_LIST = (
        ('CO','CONVEYANCING'),('LI','LITIGATION'),
        ('SY','SYARIAH'),('OT','OTHERS')
    )
    KATEGORI_PELANGGAN = (
        ('IN','INDIVIDU'),
        ('SY','SYARIKAT'),
        ('AG','AGENSI'),
        ('NG','NGO'),
        ('LL','LAIN-LAIN')
    )

    rujukan = models.CharField(max_length=70, default='')
    nama = models.CharField(max_length=120, default='')
    kategori = models.CharField(
        max_length=2, default='', choices=KATEGORI_LIST)
    kat_pelanggan = models.CharField(
        max_length=2, default='', choices=KATEGORI_PELANGGAN)


    class Meta:
        verbose_name_plural = "Client Folder"

    def __str__(self):
        return f'{self.nama}'
