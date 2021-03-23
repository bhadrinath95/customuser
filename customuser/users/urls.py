from django.urls import path, re_path
from . import views
from django.conf.urls import include
import rest_auth

app_name = 'users'


urlpatterns = [
    path('user/list/', views.UserListAPIView.as_view(), name = 'userlist'),
    path('user/detail/', views.UserDetailAPIView.as_view(), name = 'userdetail'),
    path('', include('rest_auth.urls')),
]
