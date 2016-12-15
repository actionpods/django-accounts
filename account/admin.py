from django.contrib import admin
from django import forms
from .models import *
from django.contrib.auth.models import User

class ProfileAdminForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class ProfileAdmin(admin.ModelAdmin):
    form = ProfileAdminForm


admin.site.register(Setting)
admin.site.register(Profile, ProfileAdmin)
