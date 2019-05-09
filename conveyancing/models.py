from django.db import models
from folder.models import ClientFolder


class JenisHartanah(models.Model):
    KAT_LIST = (('KED', 'KEDIAMAN'), ('PEJ', 'PEJABAT'), ('TAN', 'TANAH'))
    AKTIF_LIST = (('A', 'Aktif'), ('T', 'Tidak Aktif'))
    kategori = models.CharField(max_length=3, default='', choices=KAT_LIST)
    nama = models.CharField(max_length=250, default='')
    aktif = models.CharField(max_length=1, default='A', choices=AKTIF_LIST)

    class Meta:
        verbose_name_plural = "Jenis Hartanah"
        ordering = ('kategori', 'nama')

    def __str__(self):
        return self.kategori + ' - ' + self.nama


class Conveyancing(models.Model):
    JENIS_LIST=(('BELIAN','BELIAN'),('JUALAN','JUALAN'),
    ('PINDAH MILIK','PINDAH MILIK'),('PUSAKA','PUSAKA'))
    hartanah = models.TextField(default='')
    hartanahMalay = models.TextField(default='')
    ringkas = models.CharField(max_length=100, default='')
    jenisConveyancing = models.CharField(max_length=15, default='', choices=JENIS_LIST)
    jenisHartanah = models.OneToOneField(
        JenisHartanah, on_delete=models.CASCADE)
    penjual = models.CharField(max_length=250, default='')
    pembeli = models.CharField(max_length=250, default='')
    pemaju = models.CharField(max_length=250, default='')
    pemilik = models.CharField(max_length=250, default='')
    rujukan = models.ForeignKey(
        ClientFolder,  on_delete=models.CASCADE, blank=True)


    class Meta:
        verbose_name_plural = "Conveyancing"

    def __str__(self):
        return f'{self.hartanah}'



