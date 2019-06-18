from django import template;

register = template.Library();


@register.simple_tag
def postExcerpt(content):
    return content[0:180] + ".."
