# Generated by Django 4.1.5 on 2023-02-18 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_brand_slug_alter_product_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='img',
            field=models.ImageField(upload_to='brand/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='flag',
            field=models.CharField(choices=[('Feature', 'Feature'), ('Sale', 'Sales'), ('New', 'New')], max_length=10, verbose_name='flag'),
        ),
    ]
