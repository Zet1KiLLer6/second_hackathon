# Generated by Django 4.2.5 on 2023-09-24 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='recommend',
            field=models.ManyToManyField(blank=True, related_name='categories', to='product.category'),
        ),
    ]
