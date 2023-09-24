from django.urls import path
from applications.order.views import OrderAPIView

urlpatterns = [
    path('make/', OrderAPIView.as_view())
]
