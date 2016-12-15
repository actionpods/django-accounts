
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm


class CreateUser(CreateView):
    model=User
    template_name='registration/register.html'
    form_class=UserCreationForm
    success_url='/'
    def form_valid(self, form):
        new_user = form.save()
        new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
        login(self.request, new_user)
        return super(CreateUser, self).form_valid(form)
