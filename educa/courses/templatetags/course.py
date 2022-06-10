from django import template
register = template.Library()
# шаблонный фильтр model_name, который можно 
# применить  в  шаблонах,  чтобы  получить  имя  модели  объекта
@register.filter
def model_name(obj):
    try:
        return obj._meta.model_name
    except AttributeError:
        return None