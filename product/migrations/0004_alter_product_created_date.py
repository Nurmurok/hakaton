# Generated by Django 4.1.1 on 2022-09-26 02:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 26, 8, 10, 48, 428494)),
        ),
    ]
