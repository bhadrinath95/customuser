from django.shortcuts import render
from .serializers import UserDetailSerializer, UserListSerializer
from rest_framework.permissions import (
    IsAuthenticated, 
    IsAdminUser, 
    )
from .pagination import PostPageNumberPagination
from rest_framework.generics import ListAPIView
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
class UserListAPIView(ListAPIView):
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated,IsAdminUser]
    pagination_class = PostPageNumberPagination 
    def get_queryset(self, *args, **kwargs):
        query_list = User.objects.all()
        return query_list
    
class UserDetailAPIView(ListAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PostPageNumberPagination 
    
    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_superuser or self.request.user.is_staff:
            query_list = User.objects.all()
        else:
            query_list = User.objects.filter(id = self.request.user.id)
        return query_list