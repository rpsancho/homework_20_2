from django import template

register = template.Library()


@register.simple_tag
def mediapath(value):
    return f'/media/{str(value)}'


@register.filter
def mediapath(value):
    return f'/media/{str(value)}'
