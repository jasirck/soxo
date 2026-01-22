from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from django.shortcuts import render


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://127.0.0.1:8000/dj-rest-auth/google/"
    client_class = OAuth2Client

    def post(self, request, *args, **kwargs):
        print("GOOGLE LOGIN HIT:", request.data)
        return super().post(request, *args, **kwargs)



def google_login_page(request):
    return render(request, "google_login.html")


@receiver(user_signed_up)
def save_google_data(request, user, **kwargs):
    socialaccount = user.socialaccount_set.first()
    if not socialaccount:
        return

    data = socialaccount.extra_data
    user.first_name = data.get("given_name", "")
    user.last_name = data.get("family_name", "")
    user.email = data.get("email", user.email)
    user.save()


