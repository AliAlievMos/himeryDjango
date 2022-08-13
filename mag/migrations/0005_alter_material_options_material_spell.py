# Generated by Django 4.0.6 on 2022-07-23 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mag', '0004_material_block'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='material',
            options={'ordering': ['-spell'], 'verbose_name': 'Материал', 'verbose_name_plural': 'Материалы'},
        ),
        migrations.AddField(
            model_name='material',
            name='spell',
            field=models.CharField(default=1, max_length=50, verbose_name='Порядоковый номер автора в блоке(цифрой)'),
            preserve_default=False,
        ),
    ]
