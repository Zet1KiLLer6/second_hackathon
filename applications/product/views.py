from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from .models import Category, SpecName, Spec, Product
from .serializers import CategorySerializer, SpecNameSerializer, SpecSerializer, ProductSerializer


# Create your views here.
class CategoryAPIView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SpecNameAPIView(viewsets.ModelViewSet):
    queryset = SpecName.objects.all()
    serializer_class = SpecNameSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['name', 'cat']
    ordering_fields = ['name']
    search_fields = ['name', 'cat__name']


class SpecAPIView(viewsets.ModelViewSet):
    queryset = Spec.objects.all()
    serializer_class = SpecSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['value', 'name__name', 'name__cat__name']
    ordering_fields = ['value', 'name']


class ProductAPIView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
