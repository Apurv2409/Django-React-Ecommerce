# Generated by Django 5.0.2 on 2024-06-18 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0003_purchase_supplier_id_purchasedetails_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='purchase',
            options={'verbose_name': 'Purchase', 'verbose_name_plural': 'Purchases'},
        ),
        migrations.AlterModelOptions(
            name='purchasedetails',
            options={'verbose_name': 'Purchase Detail', 'verbose_name_plural': 'Purchase Details'},
        ),
        migrations.AlterModelOptions(
            name='purchasereturn',
            options={'verbose_name': 'Purchase Return', 'verbose_name_plural': 'Purchase Returns'},
        ),
        migrations.AlterModelOptions(
            name='purchasereturndetails',
            options={'verbose_name': 'Purchase Return Detail', 'verbose_name_plural': 'Purchase Return Details'},
        ),
    ]
