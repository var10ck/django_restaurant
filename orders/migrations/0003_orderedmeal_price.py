# Generated by Django 2.2.24 on 2021-06-12 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_orderedmeal_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderedmeal',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=11, verbose_name='Цена'),
        ),
    ]