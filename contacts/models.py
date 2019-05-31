from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Warganegara(models.Model):
    nama=models.CharField(max_length=200,default='')
    ringkas=models.CharField(max_length=50, default='', blank=True, null=True)
    int_code=models.CharField(max_length=4,default='', blank=True, null=True)

    def __str__(self):
        return self.nama


class ContactCategory(MPTTModel):
    nama = models.CharField(max_length=200, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True,
                            blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['nama']

    def __str__(self):
        return self.nama


class MyContacts(models.Model):
    nama = models.CharField(max_length=200, default='')
    ringkas = models.CharField(max_length=50, blank=True, null=True)
    no_kp_baru = models.CharField(max_length=21, default='', blank=True, null=True)
    no_kp_lama = models.CharField(max_length=21, default='', blank=True, null=True)
    no_passport=models.CharField(max_length=30, default='', blank=True, null=True)
    warganegara=models.ForeignKey(Warganegara, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama
    
    def save(self, *args, **kwargs):
        self.no_kp_baru = self.no_kp_baru.replace("-", "")
        super(MyContacts, self).save(*args, **kwargs)

    def get_contact_kp(self):
        if self.warganegara.nama=='MALAYSIA':
            if len(self.no_kp_baru) == 12:
                retkp = self.no_kp_baru[:6] + "-" + self.no_kp_baru[6:8] + "-" + self.no_kp_baru[8:]
                return retkp
            else:
                return self.no_kp_baru
        else:
            return self.no_passport


class ContactPhone(models.Model):
    KAT_LIST=(
        ('OP','Office Phone'),('PH','Phone'),('HP','Handphone'),('FAX','Fax')
    )
    PRIORITY_LIST=(
        ('PN','Primary Number'),('SN', 'Secondary Number'),('ON', 'Other Number')
    )
    nombor=models.CharField(max_length=21, default='')
    kategori=models.CharField(max_length=4, default='', choices=KAT_LIST)
    keutamaan=models.CharField(max_length=4, default='', choices=PRIORITY_LIST)
    remark=models.CharField(max_length=100,default='', blank=True,null=True)
    empunya = models.ForeignKey(
        MyContacts, on_delete=models.CASCADE, verbose_name="Owner", default=1)

    def __str__(self):
        return self.nombor


class ContactEmail(models.Model):
    KAT_LIST = (
        ('OE', 'Office Email'), ('PE', 'Personal Email'), ('OE', 'Other Email')
    )
    PRIORITY_LIST = (
        ('PE', 'Primary Email'), ('SE', 'Secondary Email'), ('OE', 'Other Email')
    )
    email = models.EmailField(max_length=100, default='')
    kategori = models.CharField(max_length=4, default='', choices=KAT_LIST)
    keutamaan = models.CharField(max_length=4, default='', choices=PRIORITY_LIST)
    remark = models.CharField(max_length=100, default='', blank=True, null=True)
    empunya = models.ForeignKey(
        MyContacts, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.email


class ContactAddress(models.Model):
    KAT_LIST = (
        ('OA', 'Office Address'), ('HA', 'Home Address'), ('OT', 'Other Address')
    )
    PRIORITY_LIST = (
        ('PE', 'Primary Address'), ('SE', 'Secondary Address'), ('OE', 'Other Address'))

    alamat1=models.CharField(max_length=200, default='', blank=True, null=True)
    alamat2=models.CharField(max_length=200, default='', blank=True, null=True)
    alamat3=models.CharField(max_length=200, default='', blank=True, null=True, help_text='optional')
    alamat4 = models.CharField(max_length=200, default='', blank=True, null=True, help_text='optional')
    poskod=models.CharField(max_length=7, default='', blank=True, null=True)
    bandar=models.CharField(max_length=100, default='', blank=True, null=True)
    bandar2=models.CharField(max_length=100, default='', blank=True, null=True, help_text='optional')
    negeri=models.CharField(max_length=100, default='', blank=True, null=True)
    negara=models.CharField(max_length=100, default='', blank=True, null=True, help_text='for other than Malaysia only')
    kategori = models.CharField(max_length=4, default='', choices=KAT_LIST)
    keutamaan = models.CharField(max_length=4, default='', choices=PRIORITY_LIST)
    remark = models.CharField(max_length=100, default='', blank=True, null=True)
    empunya = models.ForeignKey(
        MyContacts, on_delete=models.CASCADE, default=1)

    def __str__(self):
        retstr = self.alamat1 + ' ' + self.alamat2 + ' '
        if self.alamat3:
            retstr += self.alamat3 + ' '
        if self.alamat4:
            retstr += self.alamat4 + ' '
        retstr += self.poskod + ' ' + self.bandar + ' '
        if self.bandar2:
            retstr += self.bandar2 + ' '
        retstr += self.negeri
        if self.negara:
            retstr += ' ' + self.negara
        return retstr

    def get_addr_crlf(self):
        retstr = self.alamat1 + '\n' + self.alamat2 + '\n'
        if self.alamat3:
            retstr += self.alamat3 + '\n'
        if self.alamat4:
            retstr += self.alamat4 + '\n'
        retstr += self.poskod + ' ' + self.bandar + '\n'
        if self.bandar2:
            retstr += self.bandar2 + '\n'
        retstr += self.negeri
        if self.negara:
            retstr += '\n' + self.negara
        return retstr
    
    def get_addr_br(self):
        retstr = self.alamat1 + '<br>' + self.alamat2 + '<br>'
        if self.alamat3:
            retstr += self.alamat3 + '<br>'
        if self.alamat4:
            retstr += self.alamat4 + '<br>'
        retstr += self.poskod + ' ' + self.bandar + '<br>'
        if self.bandar2:
            retstr += self.bandar2 + '<br>'
        retstr += self.negeri
        if self.negara:
            retstr += '<br>' + self.negara
        return retstr
    
    class Meta:
        verbose_name_plural='Address'
