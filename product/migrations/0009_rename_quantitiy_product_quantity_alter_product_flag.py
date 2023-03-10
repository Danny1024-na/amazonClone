# Generated by Django 4.1.5 on 2023-02-18 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_brand_img_alter_product_flag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='quantitiy',
            new_name='quantity',
        ),
        migrations.AlterField(
            model_name='product',
            name='flag',
            field=models.CharField(choices=[('New', 'New'), ('Feature', 'Feature'), ('Sale', 'Sales')], max_length=10, verbose_name='flag'),
        ),
    ]
