# Generated by Django 4.0.3 on 2022-04-07 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_pappersize_statuspusinex'),
    ]

    operations = [
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('localidad', models.PositiveSmallIntegerField()),
                ('nombre', models.CharField(max_length=150)),
                ('tipo', models.CharField(max_length=1)),
                ('seccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='localidad_seccion', to='app.seccion')),
            ],
            options={
                'verbose_name_plural': 'Localidades',
            },
        ),
        migrations.AddConstraint(
            model_name='localidad',
            constraint=models.UniqueConstraint(fields=('seccion', 'localidad'), name='idxLocalidad'),
        ),
    ]