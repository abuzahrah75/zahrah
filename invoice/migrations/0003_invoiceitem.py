# Generated by Django 2.1.2 on 2019-05-28 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_auto_20190528_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=250)),
                ('item_type', models.CharField(choices=[('FEE', 'Legal Fee'), ('DIS', 'Disbursements')], default='', max_length=3)),
                ('taxed', models.BooleanField(default=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=11)),
                ('no_invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.InvoiceParticular')),
            ],
        ),
    ]
