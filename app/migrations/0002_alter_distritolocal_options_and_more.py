# Generated by Django 4.0.3 on 2022-04-07 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='distritolocal',
            options={'verbose_name': 'Distrito Local', 'verbose_name_plural': 'Distritos Locales'},
        ),
        migrations.RemoveField(
            model_name='municipio',
            name='cabecera',
        ),
    ]
