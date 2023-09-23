from django.urls import path
from applications.order.views import OrderAPIView

urlpatterns = [
    path('order/', OrderAPIView.as_view())
]
