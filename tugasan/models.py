from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class KategoriTugasan(MPTTModel):
    nama = models.CharField(max_length=200, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True,
                            blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['nama']

    def __str__(self):
        return self.nama


class TugasanTemplate(models.Model):
    pass


class TugasanConfig(models.Model):
    pass


class MyTugasan(models.Model):
    pass

