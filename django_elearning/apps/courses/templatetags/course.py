from django import template

register = template.Library()


@register.filter
def model_name(obj):
    try:
        return obj._meta.label.split('.')[-1].lower()
    except AttributeError:
        return None
