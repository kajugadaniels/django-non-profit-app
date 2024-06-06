from django import template
import re

register = template.Library()

@register.filter
def truncate_words(value, num_words=20):
    words = re.findall(r'\w+', value)
    truncated = ' '.join(words[:num_words])
    if len(words) > num_words:
        truncated += '...'
    return truncated
