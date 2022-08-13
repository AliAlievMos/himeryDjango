from django.db import models
from ckeditor.fields import RichTextField

class Authors (models.Model):
    photo = models.ImageField(upload_to='img/', verbose_name='Фото')
    name = models.CharField (max_length=50, verbose_name='Имя')
    soname = models.CharField (max_length=50, verbose_name='Фамилия')
    bio = RichTextField(null=True, blank=True,verbose_name='Биография')

    def __str__(self):
        return self.soname
        

    class Meta:
        verbose_name_plural = 'Автор_ки'
        verbose_name = 'Автор_ка'
        ordering = ['-soname']

