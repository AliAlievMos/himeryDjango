# Generated by Django 4.0.6 on 2022-08-06 17:04

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_remove_authors_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='bio',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Биография'),
        ),
    ]
