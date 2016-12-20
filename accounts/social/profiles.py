
from accounts.models import Profile

#Response is returning nothing for some reason
def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'facebook':
        profile = Profile.objects.get_or_create(user_id=user.id)[0]
        #user.email = response.get('email')
        profile.city = response.get('email')
        profile.about = "herp derp"
        profile.save()
