# Generated by Django 3.0.6 on 2020-06-12 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abm', '0013_auto_20200612_0703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='ndoc',
            field=models.BigIntegerField(verbose_name='Documento'),
        ),
    ]
