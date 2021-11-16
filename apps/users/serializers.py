from rest_framework import serializers
from django.contrib.auth import get_user_model



class UserAuthSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(max_length=500, read_only=True)
    class Meta:
        model = get_user_model()
        fields = ('id', 'auth_token', 'email', 'username', 'first_name', 'last_name', 'phone_number', 'user_type', 'is_admin', 'created', 'last_login')
        read_only_fields = fields
