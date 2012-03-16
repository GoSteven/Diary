from django.conf.urls.defaults import *
from django.contrib.auth.forms import AuthenticationForm

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.simple.redirect_to', {'url': '/diary/', }),
    (r'^diary/', include('diary.urls')),

    (r'^accounts/', include('gaeauth.urls')),
    (r'^invalid', 'django.views.generic.simple.direct_to_template',{'template':'invalid.html'}),
    #(r'.+\.html$', 'django.views.generic.simple.direct_to_template'),

)
