from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from home.models import Kategori, Partners, Solicitors, Staff
from contacts.models import *

class ClientFolder(models.Model):
    KATEGORI_PELANGGAN = (
        ('IND','INDIVIDU'),('SYA','SYARIKAT'),
        ('AGE','AGENSI'),('NGO','NGO'),
        ('LLA','LAIN-LAIN')
    )

    STATUS_LIST=(('AK','Aktif'),('TA','Tidak Aktif'),('DP','Dalam Proses'),('TG','Tangguh'),
                ('BT','Batal'),('SE','Selesai'))
    KEUTAMAAN_LIST=(('1','PALING PENTING'),('2','SANGAT PENTING'),('3','PENTING'),('4','BIASA'),
                    ('5','KURANG PENTING'),('6','TIDAK PENTING'), ('7','BOLEH ABAI'))
    rujukan = models.CharField(max_length=70, default='')
    nama = models.CharField(max_length=120, default='')
    contacts = models.ForeignKey(MyContacts,on_delete=models.CASCADE, null=True, blank=True)
    #kategori = models.CharField(max_length=3, default='', choices=KATEGORI_LIST)
    kategori = TreeForeignKey(Kategori, on_delete=models.CASCADE, null=True, blank=True)
    kat_pelanggan = models.CharField(max_length=3, default='', choices=KATEGORI_PELANGGAN)
    status_folder = models.CharField(max_length=2, default='', choices=STATUS_LIST)
    keutamaan = models.CharField(max_length=2, default='', choices=KEUTAMAAN_LIST)

    partner=models.ForeignKey(Partners, on_delete=models.CASCADE, blank=True, null=True)
    solicitor=models.ForeignKey(Solicitors, on_delete=models.CASCADE, blank=True, null=True)
    staff=models.ForeignKey(Staff, on_delete=models.CASCADE, blank=True, null=True)

    opening_date=models.DateField(blank=True, null=True)
    closing_date=models.DateField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Client Folder"

    def __str__(self):
        return f'{self.nama}'
