from django.contrib.auth import get_user_model
from django.db import models

from applications.product.models import Product

User = get_user_model()


class ProductImage(models.Model):
    """
        Картинка к продуктам
    """
    image = models.ImageField(upload_to="images/")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name="images"
    )

    def __str__(self):
        return f"{self.product.title}"


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} -> {self.product.price}"