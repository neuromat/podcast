# In myapp/admin.py

from copy import deepcopy
from django.contrib import admin
from mezzanine.blog.admin import BlogPostAdmin
from mezzanine.blog.models import BlogPost
from .models import Slider
from .models import Channel

blog_fieldsets = deepcopy(BlogPostAdmin.fieldsets)
blog_fieldsets[0][1]["fields"].insert(-2, "podcastfile")
blog_fieldsets[0][1]["fields"].insert(-3, "video")
blog_fieldsets[0][1]["fields"].insert(-1, "shortdesc")


class MyBlogPostAdmin(BlogPostAdmin):
    fieldsets = blog_fieldsets


class SliderAdmin(admin.ModelAdmin):
    list_display = ['post', 'photo']
    search_fields = ['photo']

class ChannelAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'className']
    search_fields = ['name']



admin.site.unregister(BlogPost)
admin.site.register(BlogPost, MyBlogPostAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Channel, ChannelAdmin)
