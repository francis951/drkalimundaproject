# Generated by Django 4.1.7 on 2023-04-11 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dawa', '0006_product_recieved_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='quantity',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='sale',
            name='unit_price',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
