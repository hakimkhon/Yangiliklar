from rest_framework import serializers
from .models import New, Profile

class NewSerializers(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ('id', 'author', 'title', 'content', 'photos', 'created')

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'username')