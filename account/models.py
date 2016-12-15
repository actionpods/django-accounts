from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.utils import timezone


#A User's Personal Info
class Profile(models.Model):
    user = models.OneToOneField(User)
    #Location`
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    #Personal Info
    about = models.TextField(max_length=1000, null=True, blank=True)
    def __unicode__(self):
        return '%s: %s %s' % (self.user.username,self.user.first_name, self.user.last_name)

class Setting(models.Model):
    PALETTE_THEMES = (
        ('DARK', 'Dark Theme'),
        ('LITE', 'Light Theme'),
    )
    user = models.OneToOneField(User)
    color_palette = models.CharField(max_length=4, choices=PALETTE_THEMES, default='DARK')
    def __unicode__(self):
        return self.user.username

#Forms
class UserForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ('username', 'email', 'password')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('about', 'city', 'state',)
        widgets = {
                   'about': forms.Textarea(attrs={'class':'form-control', 'rows':'5'}),
                   'city': forms.TextInput(attrs={'class':'form-control'}),
                   'state': forms.TextInput(attrs={'class':'form-control'}),
        }
