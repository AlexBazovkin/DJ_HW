# Generated by Django 4.1.1 on 2022-11-02 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0009_remove_student_teachers'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(to='school.teacher'),
        ),
    ]
