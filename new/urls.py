from django.urls import path
from .views import *

urlpatterns = [
    path('', ApiList.as_view()),
    path('<int:pk>', ApiDetail.as_view()),
    path('user/', UserList.as_view()),
    path('user/<int:pk>', UserDetail.as_view()),
]
