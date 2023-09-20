from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from applications.account.serializers import RegisterSerializer, ChangePasswordSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

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


class ChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            old_password = serializer.validated_data.get('old_password')
            new_password = serializer.validated_data.get('new_password')


            if not user.check_password(old_password):
                return Response({'detail': 'Старый пароль неверен'}, status=status.HTTP_400_BAD_REQUEST)


            user.set_password(new_password)
            user.save()

            return Response({'detail': 'Пароль успешно изменен'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


