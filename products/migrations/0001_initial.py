# Generated by Django 4.1.2 on 2022-10-05 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Category Type')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Category Description')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, verbose_name='Product Name')),
                ('product_price', models.FloatField(verbose_name='unit price')),
                ('available_qty', models.FloatField(default=0, verbose_name='Available Quantity')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Product Description')),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='products/images', verbose_name='Product Image')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_category', to='products.category', verbose_name='Product Category')),
            ],
        ),
    ]
