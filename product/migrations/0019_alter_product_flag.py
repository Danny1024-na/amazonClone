# Generated by Django 4.1.5 on 2023-03-13 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_alter_product_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='flag',
            field=models.CharField(choices=[('Feature', 'Feature'), ('New', 'New'), ('Sale', 'Sale')], max_length=10, verbose_name='flag'),
        ),
    ]
