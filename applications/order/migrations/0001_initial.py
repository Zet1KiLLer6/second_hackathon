<<<<<<< HEAD
# Generated by Django 4.2.5 on 2023-09-22 14:08
=======
# Generated by Django 4.2.5 on 2023-09-22 13:55
>>>>>>> product_recommendation-adil

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.CharField(choices=[('PAID', 'Оплачивается'), ('ORDER_PROCCESING', 'Обратботка заказа')], default='PAID', max_length=22, verbose_name='Статус заказа')),
                ('order_comment', models.TextField(blank=True, null=True)),
                ('order_create_at', models.DateTimeField(auto_now_add=True)),
                ('signer_firstname', models.CharField(max_length=50, verbose_name='Имя заказчика')),
                ('signer_lastname', models.CharField(max_length=50, verbose_name='Фамилия заказчика')),
                ('signer_address', models.CharField(max_length=1000, verbose_name='Адрес доставки')),
                ('signer_phone', models.CharField(max_length=11, verbose_name='Контактный телефон')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=1, verbose_name='Количетсво')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_items', to='product.product')),
            ],
            options={
                'verbose_name': 'Позиция заказа',
                'verbose_name_plural': 'Позиции заказов',
            },
        ),
    ]