from django import template;
from ..models import Slider


register = template.Library()


@register.simple_tag
def postExcerpt(content):
    return content[0:180] + ".."



@register.simple_tag
def sampleContent(post, mediaurl):

    string = "";

    for i in Slider.objects.all():
        if i.post == post:
            string += '<img class="post-gallery-item" width="100px" src="' + mediaurl + str(i.photo) + '" /> '

    print(string)
    return string