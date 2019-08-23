from django import template;
from html import unescape

from ..models import Slider
from ..models import Channel

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
            string += '<img class="post-gallery-item" title="Foto:' + i.credit + '" width="100px" src="' + mediaurl + str(i.photo) + '" /> '
    return string

@register.simple_tag
def podcast_channels():

    def handleicons(classname):

        if classname == 'link-rss':
            return '<i class="fa fa-rss"></i>'
        elif classname == 'email':
            return '<i class="far fa-envelope"></i>'
        elif classname == 'spotify':
            return '<i class="fab fa-spotify"></i>'
        elif classname == 'itunes':
            return '<i class="fab fa-itunes"></i>'
        elif classname == 'soundcloud':
            return '<i class="fab fa-soundcloud"></i>'
        elif classname == 'bullhorn':
            return '<i class="fas fa-bullhorn"></i>'
        else:
            return '<i class="fas fa-podcast"></i>'

    string = ''
    for i in Channel.objects.all():
        string += '<a class="share-box-item ' + i.className + '" target="_blank" href="' + i.url + '" title="' + i.name +'" >'+ handleicons(i.className) + ' <span>' + i.name + '</span></a>'

    return string