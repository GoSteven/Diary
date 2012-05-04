__author__ = 'steveny'

from django import template
import datetime

register = template.Library()

def applytimezone(value, arg=''):
    #10 hour time difference between appengine and sydney
    if isinstance(value, datetime.datetime):
        return value + datetime.timedelta(hours=10)
    return value

register.filter('applytimezone', applytimezone)