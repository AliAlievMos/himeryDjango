from django.db import models
from authors.models import Authors
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from  embed_video.fields  import  EmbedVideoField



class Number(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название номера')
    anotation_head = models.CharField(max_length=50, verbose_name='Заголовок аннотации')
    anotation = RichTextField(null=True, blank=True, verbose_name='Аннотация')
    published = models.DateTimeField(auto_now_add=True, db_index=True)
    published_str = models.CharField(max_length=50, verbose_name='дата выпуска')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Номера'
        verbose_name = 'Номер'
        ordering = ['-name']

class Block(models.Model):
    number = models.ForeignKey('Number', null=True, on_delete=models.PROTECT,related_name='number', verbose_name='Номер')
    anotation = RichTextField(null=True, blank=True, verbose_name='Аннотация')
    spell = models.CharField(max_length=50, verbose_name='Порядоковый номер блока(цифрой)')
    name = models.CharField(max_length=50, verbose_name='Название блока')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Блоки'
        verbose_name = 'Блок'
        ordering = ['-spell']

class Material(models.Model):
    name = models.CharField(max_length=50, verbose_name='Оглавление материала')
    text = RichTextField(null=True, blank=True, verbose_name='Текст')
    auth = models.ForeignKey(Authors, null=True, on_delete=models.PROTECT, verbose_name='Автор')
    block = models.ForeignKey('Block', null=True, on_delete=models.PROTECT, related_name='block', verbose_name='Блок')
    number = models.ForeignKey('Number', null=False, on_delete=models.PROTECT, related_name='numberr', verbose_name='Номер')    
    spell = models.CharField(max_length=50, verbose_name='Порядоковый номер автора в блоке(цифрой)')
    video2 = EmbedVideoField(blank=True, null=True, verbose_name='Видео' )


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Материалы'
        verbose_name = 'Материал'
        ordering = ['-spell']
