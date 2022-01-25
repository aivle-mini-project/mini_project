from django import template
register = template.Library()

@register.filter(name='show')
def show(value):
    if value =='negative':
        return '부정적이네요, 오늘 기분이 안 좋나요?'
    elif value =='neutral':
        return '편안하시네요'
    else:
        return '행복한 하루인가요'