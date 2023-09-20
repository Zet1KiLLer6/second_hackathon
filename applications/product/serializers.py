from rest_framework import serializers

from .models import Category, SpecName, Spec, Product


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()

    class Meta:
        model = Category
        fields = "__all__"


class SpecSerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()

    class Meta:
        model = Spec
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.update({
            'name': instance.name.name
        })
        return rep


class SpecNameSerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()
    values = SpecSerializer(many=True, read_only=True)

    class Meta:
        model = SpecName
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = "__all__"
        extra_kwargs = {
            'specs': {'required': False}
        }

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.update({
            'specs': SpecSerializer(instance.specs.all(), many=True).data
        })
        return rep

    def validate(self, attrs):
        if attrs.get('images', None):
            serializers.ValidationError({'images': ['required']})
        return attrs