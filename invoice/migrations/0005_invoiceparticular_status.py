# Generated by Django 2.1.2 on 2019-05-31 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0004_auto_20190528_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoiceparticular',
            name='status',
            field=models.CharField(choices=[('OP', 'Open'), ('CL', 'Close'), ('PE', 'Pending')], default='OP', max_length=2),
        ),
    ]
