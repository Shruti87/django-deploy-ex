from django import template

register = template.Library()

def cut_out(value,arg):
    """
    This cuts out arg from value string.
    """
    return value.replace(arg,'')

register.filter('cut_out',cut_out)
