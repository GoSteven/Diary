from django.core.cache import cache
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.simple import direct_to_template
from django.http import HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from diary.forms import CreateGreetingForm
from diary.models import Greeting
import random

MEMCACHE_GREETINGS = 'greetings'
items_per_page = 10

def list_greetings(request):
    page_number = 1
    try:
        page_number = int(request.GET.get('p','1'))
    except ValueError:
        page_number = 1
    greetings = cache.get(MEMCACHE_GREETINGS + str(page_number))
    if greetings is None:
        greetings = Greeting.objects.all().order_by('-date')[(page_number-1)*items_per_page:page_number*items_per_page]
        cache.add(MEMCACHE_GREETINGS + str(page_number), greetings)
    return direct_to_template(request, 'diary/index.html',
                              {'greetings': greetings,
                               'form': CreateGreetingForm(),
                               'nextpage': page_number + 1,
                               'aniv': random.randint(0,10) == 7})

def create_greeting(request):
    if request.method == 'POST' and request.user.is_authenticated():
        form = CreateGreetingForm(request.POST)
        if form.is_valid():
            greeting = form.save(commit=False)
            if request.user.is_authenticated():
                greeting.author = request.user
            greeting.save()
            for i in range(1, Greeting.objects.all().count() / items_per_page + 2):
                cache.delete(MEMCACHE_GREETINGS + str(i))
    return HttpResponseRedirect('/diary/')

def login(request):
    redirect_to = settings.LOGIN_REDIRECT_URL
    return HttpResponseRedirect(redirect_to)