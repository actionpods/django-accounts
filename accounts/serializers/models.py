from django.forms import widgets
from rest_framework import serializers
from django.contrib.auth.models import User
from ..models import Profile

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'email', 'password', 'username')

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    email = serializers.ReadOnlyField(source='user.email')
    class Meta:
        model = Profile
        fields = ('url', 'user', 'username', 'email', 'city', 'state', 'about')
