from rest_framework import serializers

from .models import Category, SpecName, Spec, Product
from ..feedback.serializers import LikeSerializer, CommentSerializer, ProductImageSerializer


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
    likes = LikeSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source="owner.email")
    comments = CommentSerializer(many=True, read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
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

        rep["like_count"] = instance.likes.filter(is_like=True).count()

        rating_result = 0
        for rating in instance.ratings.all():
            rating_result += rating.rating

        if rating_result:
            rep["rating"] = rating_result / instance.ratings.all().count()
        else:
            rep["rating"] = 0

        return rep