# Generated by Django 4.0.6 on 2022-07-21 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mag', '0002_alter_number_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='number',
            name='published_str',
            field=models.CharField(default=1, max_length=50, verbose_name='дата выпуска'),
            preserve_default=False,
        ),
    ]
