# Generated by Django 4.1.5 on 2023-01-31 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0011_students_age_students_family_l_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='sex',
        ),
    ]
