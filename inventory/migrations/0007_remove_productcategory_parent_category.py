# Generated by Django 3.1.5 on 2021-01-29 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategory',
            name='parent_category',
        ),
    ]