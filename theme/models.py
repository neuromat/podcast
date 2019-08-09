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