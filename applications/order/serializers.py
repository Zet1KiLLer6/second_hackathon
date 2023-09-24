from rest_framework import serializers
from applications.order.models import Order
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from applications.order.services import send_order_confirmed
from rest_framework.response import Response


User = get_user_model()


class OrderSerializer(serializers.Serializer):
    signer_firstname = serializers.CharField(required=True)
    signer_lastname = serializers.CharField(required=True)
    signer_address = serializers.CharField(required=True)
    signer_phone = serializers.CharField(required=True)
    order_amount = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        user = get_object_or_404(User, email=self.validated_data.get('email'))
        send_order_confirmed(user.email, Order.order_number)
        return user
