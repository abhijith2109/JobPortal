# Generated by Django 4.0.4 on 2022-06-21 18:59

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0010_alter_jobs_last_date_alter_jobs_qualification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='job_description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
