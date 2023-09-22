from django.db import models
from django.contrib.auth import get_user_model
from applications.product.models import Product

User = get_user_model()

class Order(models.Model):
    """
        Модель для информации о заказе
    """

    STATUS = (
        ('PAID', 'Оплачивается'),
        ('ORDER_PROCCESING', 'Обратботка заказа'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_status = models.CharField('Статус заказа', choices=STATUS, default='PAID', max_length=22)
    order_comment = models.TextField(blank=True, null=True)
    order_create_at = models.DateTimeField(auto_now_add=True)

    signer_firstname = models.CharField('Имя заказчика', max_length=50)
    signer_lastname = models.CharField('Фамилия заказчика', max_length=50)
    signer_address = models.CharField('Адрес доставки', max_length=1000)
    signer_phone = models.CharField('Контактный телефон', max_length=11)

    def __str__(self):
        return f'Заказ №{self.pk}'


class OrderItem(models.Model):
    """
        Модель товара в заказе
    """

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_items')
    amount = models.PositiveIntegerField('Количетсво', default=1)

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказов'

    def __str__(self):
        return f'{self.product.slug} --- {self.product.name}'
