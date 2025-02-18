# Generated by Django 5.0.3 on 2024-03-23 08:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_alter_area_options_alter_city_options_and_more'),
        ('user', '0005_remove_customer_address_customer_area_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='area_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='address.area'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='mobile',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
