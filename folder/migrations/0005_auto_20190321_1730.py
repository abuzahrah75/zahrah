# Generated by Django 2.1.2 on 2019-03-21 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folder', '0004_auto_20190321_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientfolder',
            name='kat_pelanggan',
            field=models.CharField(choices=[('IND', 'INDIVIDU'), ('SYA', 'SYARIKAT'), ('AGE', 'AGENSI'), ('NGO', 'NGO'), ('LLA', 'LAIN-LAIN')], default='', max_length=3),
        ),
    ]