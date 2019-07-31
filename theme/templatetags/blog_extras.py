from django import template;
from html import unescape

from ..models import Slider


register = template.Library()

@register.simple_tag
def postLargeExcerpt(content):
    return content[0:350] + ".."

@register.simple_tag
def postExcerpt(content):
    return content[0:180] + ".."

@register.simple_tag
def postShortExcerpt(content):
    return unescape(content[0:80] + "..")


@register.simple_tag
def postGallery(post, mediaurl):

    string = ""

    for i in Slider.objects.all():
        if i.post == post:
             string += '<img class="post-gallery-item" width="100px" src="' + mediaurl + str(i.photo) + '" /> '
            # string += '<div class="post-gallery-item" width="100px; height: 140px;" style="background-image:url(' + mediaurl + str(i.photo) + ')" ></div> '
    return string