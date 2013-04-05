from django import template

register = template.Library()


@register.filter
def type(value):
    return type(value)

@register.filter
def classname(obj):
    classname = obj.__class__.__name__
    return classname
