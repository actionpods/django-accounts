from django.conf.urls import url, include

from .views import main

urlpatterns = [
               url('^', include('django.contrib.auth.urls')),
               url('^register/$', main.CreateUser.as_view(), name="register"),
               ]

''' Includes the following URLs:
^login/$ [name='login']
^logout/$ [name='logout']
^password_change/$ [name='password_change']
^password_change/done/$ [name='password_change_done']
^password_reset/$ [name='password_reset']
^password_reset/done/$ [name='password_reset_done']
^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='password_reset_confirm']
^reset/done/$ [name='password_reset_complete']
'''
