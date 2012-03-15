from django.conf import settings
from django.contrib.auth.models import User
from google.appengine.api import users

class GoogleBackend:
    def authenticate(self, username=None, password=None):
        login_valid = (settings.ADMIN_LOGIN == username)
        user = users.get_current_user()
        if (user and user.email() == 'yousilin@gmail.com' or user.email() == 'mendymeng.1206@gmail.com'):
            login_valid = true;
        else:
            login_valid = false;
        if login_valid:
            try:
                user = User.objects.get(username=user.email())
            except User.DoesNotExist:
                # Create a new user. Note that we can set password
                # to anything, because it won't be checked; the password
                # from settings.py will.
                user = User(username=username, password='get from settings.py', last_name=user.nickname())
                user.is_staff = True
                user.is_superuser = True
                user.save()
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None



