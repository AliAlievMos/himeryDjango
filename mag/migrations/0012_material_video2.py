# Generated by Django 4.0.6 on 2022-08-13 13:42

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mag', '0011_remove_material_body_material_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='video2',
            field=embed_video.fields.EmbedVideoField(blank=True, null=True, verbose_name='Видео'),
        ),
    ]
