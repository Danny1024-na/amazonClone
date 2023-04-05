# Generated by Django 4.1.5 on 2023-04-05 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_alter_product_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='flag',
            field=models.CharField(choices=[('Feature', 'Feature'), ('Sale', 'Sale'), ('New', 'New')], max_length=10, verbose_name='flag'),
        ),
    ]
