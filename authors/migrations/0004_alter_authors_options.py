# Generated by Django 4.0.6 on 2022-08-08 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0003_alter_authors_bio'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authors',
            options={'ordering': ['-soname'], 'verbose_name': 'Автор_ка', 'verbose_name_plural': 'Автор_ки'},
        ),
    ]
