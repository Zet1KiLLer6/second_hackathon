# Generated by Django 4.2.5 on 2023-09-22 13:55

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('slug', models.SlugField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=127)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childs', to='product.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=247)),
                ('description', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('available', models.PositiveIntegerField()),
                ('views', models.PositiveIntegerField(default=0)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.category')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='SpecName',
            fields=[
                ('slug', models.SlugField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=127)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spec_names', to='product.category')),
            ],
        ),
        migrations.CreateModel(
            name='Spec',
            fields=[
                ('slug', models.SlugField(primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=80)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='values', to='product.specname')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='specs',
            field=models.ManyToManyField(blank=True, related_name='products', to='product.spec'),
        ),
    ]
