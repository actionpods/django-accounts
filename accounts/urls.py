from django.conf.urls import url

from .views import main

urlpatterns = [
               url(r'^$', main.profile_private, name='account'),
               url(r'^register$', main.register, name='register'),
               url(r'^logout$', main.logout_view, name='logout'),
               url(r'^login$', main.login_view, name='login'),
               url(r'^social$', main.login_social, name='login_social'),
               url(r'^profile$', main.profile_private, name='profile'),
               url(r'^public/(?P<username>[^\.]+)/$', main.profile_public, name='public'),

               ]
