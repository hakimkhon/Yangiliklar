from django.shortcuts import render
from .models import New, Profile
from .serializers import NewSerializers, UserSerializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView

class ApiList(ListCreateAPIView):
    queryset = New.objects.all()
    serializer_class = NewSerializers

class ApiDetail(RetrieveUpdateAPIView, RetrieveDestroyAPIView):
    queryset = New.objects.all()
    serializer_class = NewSerializers

class UserList(ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserSerializers

class UserDetail(RetrieveUpdateAPIView, RetrieveDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserSerializers

