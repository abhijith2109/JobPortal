# Generated by Django 4.0.4 on 2022-05-18 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0002_jobss'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobss',
            old_name='locAation',
            new_name='location',
        ),
    ]