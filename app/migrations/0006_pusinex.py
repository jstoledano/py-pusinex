# Generated by Django 4.0.3 on 2022-04-11 01:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_localidad_localidad_idxlocalidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pusinex',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_levantamiento', models.DateField()),
                ('localidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pusinex_localidad', to='app.localidad')),
                ('status_pusinex', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pusinex_status', to='app.statuspusinex')),
            ],
        ),
    ]