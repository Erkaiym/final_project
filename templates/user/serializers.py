#from django.contrib.auth import User, Group
from rest_framework import serializers
from .models import User, Profile

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'userna')