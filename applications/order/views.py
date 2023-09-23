from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Order
from applications.order.serializers import OrderSerializer

User = get_user_model()


class OrderAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, reqeust):
        serializer = OrderSerializer(data=reqeust.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
