__author__ = 'steveny'
class GoogleBackend:
    def authenticate(self, request, google_user):
        try:
            prof = GoogleProfile.objects.get(google_user_id=google_user.user_id())
            return prof.user
        except GoogleProfile.DoesNotExist:

            # ...[snip]... deal with our django user, email, nickname etc here

            # a new profile will need to be tied to an existing ServiceProvider, so get the correct instance (i.e. google) here
            sp = get_service_provider("google") # call utility method to get a model instance

            # create a new google profile
            newprofile = GoogleProfile.objects.create(
                serviceprovider = sp,
                user = user,
                google_user_id = google_user.user_id(),
                screen_name = nickname,
                email = email)
            newprofile.save()

            return user

