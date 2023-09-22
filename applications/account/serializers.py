from rest_framework import serializers
from django.contrib.auth import get_user_model

# from applications.account.services import send_activation_code
from applications.account.tasks import celery_send_activation_code

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password_again = serializers.CharField(required=True, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password_again')

    def validate_email(self, email):
        return email

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.pop('password_again')

        if password != password2:
            raise serializers.ValidationError('Первый и Второй пароли не совпадают!')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        celery_send_activation_code.delay(user.email, user.code)
        return user

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
