# Generated by Django 3.0.6 on 2020-06-12 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abm', '0016_auto_20200612_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='up',
            name='date',
            field=models.CharField(max_length=10, verbose_name='Fecha'),
        ),
    ]