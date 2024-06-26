from django import template

register = template.Library()

ESK = ['редиск',]


@register.filter()
def censor(value):
    for i in ESK:
        value = value.replace(i[1:], '*' * len(i[1:]))
    return value


