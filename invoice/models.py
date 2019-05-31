from django.db import models
from folder.models import ClientFolder

class InvoiceParticular(models.Model):
    STATUS_LIST=(
        ('OP','Open'),('CL','Close'),
        ('PE','Pending')
    )
    folder = models.ForeignKey(ClientFolder, on_delete=models.CASCADE)
    bil_no = models.CharField(max_length=100, default="Proforma Invoice")
    open_date = models.DateField()
    close_date = models.DateField(blank=True, null=True)
    #part1 = models.CharField(max_length=250 ,blank=True, null=True)
    part1= models.TextField()
    part2 = models.TextField(blank=True, null=True)
    part3 = models.TextField(blank=True, null=True)
    part4 = models.TextField(blank=True, null=True)
    part5 = models.TextField(blank=True, null=True)

    taxed = models.DecimalField(
        max_digits=9, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(
        max_digits=11, decimal_places=2, blank=True, null=True)
    status= models.CharField(max_length=2,choices=STATUS_LIST, default='OP')

    def __str__(self):
        return self.folder.rujukan + " -> RM" + str(self.total)

class InvoiceItem(models.Model):
    TYPE_LIST = (('FEE','Legal Fee'),('DIS','Disbursements'))
    no_invoice = models.ForeignKey(InvoiceParticular, on_delete=models.CASCADE)
    item = models.CharField(max_length=250)
    item_type = models.CharField(max_length=3, default='', choices=TYPE_LIST)
    taxed = models.BooleanField(default=False)
    amount = models.DecimalField(max_digits=11, decimal_places=2)

    def __str__(self):
        return self.item + " (" + str(self.amount) + ")"
