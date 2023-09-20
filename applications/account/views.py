from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from applications.account.serializers import RegisterSerializer, LoginSerializer


User = get_user_model()

class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response('Регистрация прошла успешно! Код активации был отправлен вам на почту', status=201)


class ActivationAPIView(APIView):
    def get(self, request, code):
        user = get_object_or_404(User, code=code)
        user.is_active = True
        user.code = ''
        user.save(update_fields=('is_active', 'code'))
        return Response('Регистрация прошла успешно!', status=200)
