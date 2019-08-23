from django.db import models
from mezzanine.blog.models import BlogPost

class Slider(models.Model):
    post = models.ForeignKey(BlogPost)
    photo = models.ImageField()
    credit = models.CharField(max_length=100, default='')

    # def __str__(self):
    #     return self.photo

    class Meta:
        verbose_name = 'Imagem galeria'
        verbose_name_plural = 'Imagens galeria'


class Channel(models.Model):
    name = models.CharField(max_length=100, default='')
    url = models.CharField(max_length=200, default= '')
    className = models.CharField(max_length=100, default='')

    class Meta:
        verbose_name = 'Canal'
        verbose_name_plural = 'Canais'