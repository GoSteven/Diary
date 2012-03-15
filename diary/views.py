from django.core.cache import cache
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.simple import direct_to_template
from django.http import HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from diary.forms import CreateGreetingForm
from diary.models import Greeting

MEMCACHE_GREETINGS = 'greetings'

def list_greetings(request):
    greetings = cache.get(MEMCACHE_GREETINGS)
    if greetings is None:
        greetings = Greeting.objects.all().order_by('-date')[:10]
        cache.add(MEMCACHE_GREETINGS, greetings)
    return direct_to_template(request, 'diary/index.html',
                              {'greetings': greetings,
                               'form': CreateGreetingForm()})

def create_greeting(request):
    if request.method == 'POST':
        form = CreateGreetingForm(request.POST)
        if form.is_valid():
            greeting = form.save(commit=False)
            if request.user.is_authenticated():
                greeting.author = request.user
            greeting.save()
            cache.delete(MEMCACHE_GREETINGS)
    return HttpResponseRedirect('/diary/')

def create_new_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # user must be active for login to work
            user.is_active = True
            user.save()
            return HttpResponseRedirect('/diary/')
    else:
        form = UserCreationForm()
    return direct_to_template(request, 'diary/user_create_form.html',
        {'form': form})

def login(request):
    redirect_to = settings.LOGIN_REDIRECT_URL
    return HttpResponseRedirect(redirect_to)