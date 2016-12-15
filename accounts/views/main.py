
from django.contrib.auth import logout,authenticate, login
from django.utils import timezone
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.http.response import HttpResponse, HttpResponseRedirect
from django.template.context_processors import csrf
from django.contrib import auth
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import PermissionDenied

from django.db.models import Sum, F, FloatField, Q, IntegerField

from ..models import *
from django.contrib.auth.models import User

from .social_media import *

from ..serializers.models import UserSerializer
from ..serializers.forms import LoginSerializer

def login_view(request):
    args = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                args['login_status'] = "WELCOME"
            else:
                args['login_status'] = "Disabled User"
        else:
            # Return an 'invalid login' error message.
            args['login_status'] = "Invalid Login"
    return redirect('/', args)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

# A Listing of all employees on the site
def profile_listing(request):
    args = {
        "profiles": Profile.objects.all()
    }
    return render(request, 'account/index.html', args)

# The user's personal profile - Should be viewable by ONLY that user
def profile_private(request):
    args = {}
    return render_to_response('account/profile_private.html', RequestContext(request,args))

def profile_public(request, username):
    args = {
        "profile": get_object_or_404(User, username=username)
    }
    return render_to_response('account/profile_public.html', RequestContext(request,args))


def register(request):
    if request.user.is_authenticated():
        return redirect('/')
    userform = UserForm(request.POST or None, prefix='user')
    profileform = ProfileForm(request.POST or None, prefix='profile')
    args = {}
    if request.method == 'POST':
        if userform.is_valid() and profileform.is_valid():
            if userform.cleaned_data["confirm_password"] and userform.cleaned_data["password"] == userform.cleaned_data["confirm_password"]:
                user = userform.save()
                #Set email as username
                user.email = userform.cleaned_data['username']
                user.set_password(user.password)
                user.save()
                profile = profileform.save(commit=False)
                profile.user = user
                profile.save()
                #After succesful auth, login user
                new_user = authenticate(username=userform.cleaned_data['username'],
                                        password=userform.cleaned_data['password'])
                login(request, new_user)
                return redirect('/', RequestContext(request,args))
    args['userform'] = userform
    args['profileform'] = profileform
    return render(request, 'account/login.html', args)
