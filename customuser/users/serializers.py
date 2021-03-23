from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()
        
class UserListSerializer(ModelSerializer):
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = [
                'full_name',
            ]
        
    def get_fullname(self, obj):
        return obj.first_name +" "+obj.last_name
    
class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
                'first_name',
                'last_name',
                'email',
                'gender',
                'date_of_birth',
                'photo',
            ]