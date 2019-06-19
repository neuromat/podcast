from django.db import models
from mezzanine.blog.models import BlogPost


class Slider(models.Model):
    post = models.ForeignKey(BlogPost)
    photo = models.ImageField()

    # def __str__(self):
    #     return self.photo