# Generated by Django 2.1.2 on 2019-05-27 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20190526_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactaddress',
            name='empunya',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contacts.MyContacts'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactemail',
            name='empunya',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.MyContacts'),
        ),
        migrations.AlterField(
            model_name='contactphone',
            name='empunya',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.MyContacts', verbose_name='Owner'),
        ),
    ]
