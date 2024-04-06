from django import template
import os

register = template.Library()

@register.filter
def basename(value):
    if hasattr(value, 'name'):
       
        return value.name.split('/')[-1] 
    else:
        return ''
    
    
# import os
# from django import template

# register = template.Library()

# @register.filter
# def basename(value):
#     return os.path.basename(value)

# import os
# from django import template

# register = template.Library()

# @register.filter
# def basename(value):
#     return os.path.basename(value)