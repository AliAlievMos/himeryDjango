from django.db import models

class Contacts (models.Model):
    cont = models.TextField(null=True, blank=True,verbose_name='Контакты')

    class Meta:
        verbose_name_plural = 'Контакты'
        verbose_name = 'Контакт'
        # ordering = ['-сont']