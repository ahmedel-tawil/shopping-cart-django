# Generated by Django 4.1.2 on 2022-10-06 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0003_itemunit'),
        ('products', '0003_product_price_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='unit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='utilities.itemunit', verbose_name='Unit'),
            preserve_default=False,
        ),
    ]
