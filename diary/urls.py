from django.conf.urls.defaults import *

urlpatterns = patterns('diary.views',
    (r'^$', 'list_greetings'),
    (r'^sign$', 'create_greeting')
)