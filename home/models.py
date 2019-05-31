from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Kategori(MPTTModel):
    nama = models.CharField(max_length=200, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, 
        blank=True,related_name='children')

    class MPTTMeta:
        order_insertion_by=['nama']

    def __str__(self):
        return self.nama


class Cawangan(models.Model):
    nama = models.CharField(max_length=200, unique=True)
    ringkas = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.ringkas


class Partners(models.Model):
    nama = models.CharField(max_length=200, default='')
    initial = models.CharField(max_length=21, default='', blank=True, null=True)

    def __str__(self):
        return self.nama

class Solicitors(models.Model):
    nama = models.CharField(max_length=200, default='')
    initial = models.CharField(
        max_length=21, default='', blank=True, null=True)

    def __str__(self):
        return self.nama

class Staff(models.Model):
    nama = models.CharField(max_length=200, default='')
    initial = models.CharField(
        max_length=21, default='', blank=True, null=True)
        
    def __str__(self):
        return self.nama
