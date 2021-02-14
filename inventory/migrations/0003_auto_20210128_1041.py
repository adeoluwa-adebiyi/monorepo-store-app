# Generated by Django 3.1.5 on 2021-01-28 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20210128_1031'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductListing',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='listing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.productlisting'),
        ),
    ]