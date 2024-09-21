import logging
from django import template

logger = logging.getLogger(__name__)
register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()


@register.filter(name='times')
def times(number):
    return range(number)
