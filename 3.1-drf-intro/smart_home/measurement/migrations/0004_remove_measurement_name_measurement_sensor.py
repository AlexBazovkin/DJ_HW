# Generated by Django 4.1.1 on 2022-11-19 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0003_alter_measurement_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measurement',
            name='name',
        ),
        migrations.AddField(
            model_name='measurement',
            name='sensor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='measurement.sensor'),
            preserve_default=False,
        ),
    ]
