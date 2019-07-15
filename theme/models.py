from django.db import models
from mezzanine.blog.models import BlogPost

class Slider(models.Model):
    post = models.ForeignKey(BlogPost)
    photo = models.ImageField()

    def __str__(self):
        return self.post, self.post.publish_date.strftime("%d/%m/%Y"),   self.photo
