# Generated by Django 4.1.1 on 2022-10-30 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_alter_student_teachers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(to='school.teacher'),
        ),
    ]
