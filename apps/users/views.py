
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.status import (HTTP_201_CREATED, HTTP_200_OK, HTTP_400_BAD_REQUEST)

from apps.users.models import APPUser
from apps.users.serializers import UserAuthSerializer

class UserSignUp(APIView):
    model = get_user_model()
    permission_classes = (AllowAny, )

    def post(self, request):
        first_name = request.data.get('first_name', None)
        last_name = request.data.get('last_name', None)
        password = request.data.get('password', None)
        phone_number = request.data.get('phone_number', None)
        email = request.data.get('email', None) 
   
        if first_name is not None and last_name is not None and phone_number is not None and password is not None and email is not None:
            
            username = '%s%s'%(first_name, last_name)
            user = APPUser(email=email, first_name=first_name, last_name=last_name, username=username, phone_number=phone_number, user_type="APP USER")
            user.set_password(password)
            user.save()
            myuser = UserAuthSerializer(user, context={'request': request})
            return Response({'message': 'signup successful.', 'status': 'success', 'results': myuser.data}, status=HTTP_201_CREATED)
        return Response({'message': 'please supply all required parameters', 'status': 'failed'}, status=HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    model = get_user_model()
    permission_classes = (AllowAny, )

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            user = UserAuthSerializer(user, context={'request': request})
            return Response({'message': 'login successful.', 'status': 'success', 'results': user.data}, status=HTTP_200_OK)
        return Response({'message': 'Incorrect credentials', 'status': 'failed'}, status=HTTP_400_BAD_REQUEST)
    