# Generated by Django 4.1.1 on 2022-09-26 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_vendor',
            field=models.CharField(blank=True, choices=[('vendor', 'vendor'), ('customer', 'customer')], max_length=255, null=True),
        ),
    ]
