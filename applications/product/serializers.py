from rest_framework import serializers

from .models import Category, SpecName, Spec, Product, ProductImage


class CategoryListSerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()
    childs = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('name', 'slug', 'parent', 'childs',)

    def get_childs(self, obj):
        return CategoryListSerializer(obj.get_children(), many=True).data


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug', 'parent',)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.update({
            'filters': SpecNameSerializer(SpecName.objects.filter(cat__in=instance.get_descendants(include_self=True)), many=True).data
        })
        return rep


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


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"


class ProductListSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('name', 'price', 'slug', 'available', 'images')


class ProductDetailSerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at')
        extra_kwargs = {
            'specs': {'required': False}
        }

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.update({
            'specs': SpecSerializer(instance.specs.all(), many=True).data
        })
        return rep

    def create(self, validated_data):
        images = self.context.get('request').FILES.getlist('images')
        product = super().create(validated_data)

        if not images:
            raise serializers.ValidationError({'images': 'Хотя бы одна фотография должна быть загружена'})

        ProductImage.objects.bulk_create([ProductImage(product=product, image=image) for image in images])

        return product
