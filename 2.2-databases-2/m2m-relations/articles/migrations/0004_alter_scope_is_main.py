# Generated by Django 4.1.1 on 2022-11-17 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_scope_is_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scope',
            name='is_main',
            field=models.BooleanField(default='False', verbose_name='Основной'),
        ),
    ]