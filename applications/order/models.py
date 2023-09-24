import random
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
        ('ORDER_PROCCESING', 'Обработка заказа'),
        ('SUCCESFULLY', 'Успешно ожидайте заказ в течение недели'),
        ('WAITING', 'Ваш заказ прибудет через 4 дня'),
        ('ARRIVED', 'Ваш заказ прибыл!'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_status = models.CharField('Статус заказа', choices=STATUS, default='PAID', max_length=22)
    order_comment = models.TextField(blank=True, null=True)
    order_create_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(null=True, blank=True)

    signer_firstname = models.CharField('Имя заказчика', max_length=50)
    signer_lastname = models.CharField('Фамилия заказчика', max_length=50)
    signer_address = models.CharField('Адрес доставки', max_length=1000)
    signer_phone = models.CharField('Контактный телефон', max_length=11)

    order_number = models.CharField('Номер заказа', max_length=6, unique=True, default='')

    import random

    def generate_order_number(self):
        return ''.join(str(random.randint(1, 9)) for _ in range(6))

    def save(self, *args, **kwargs):
        if not self.order_number:
            while True:
                random_number: object = self.generate_order_number()
                if not Order.objects.filter(order_number=random_number).exists():
                        self.order_number = random_number
                        break
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f'Заказ №{self.order_number}'


class OrderItem(models.Model):
    """
        Модель товара в заказе
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_items')
    amount = models.PositiveIntegerField('Количество', default=1)

