from django.db import models
from folder.models import ClientFolder

class Conveyancing(models.Model):
    hartanah = models.TextField(default='')
    ringkas = models.CharField(max_length=100, default='')
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

