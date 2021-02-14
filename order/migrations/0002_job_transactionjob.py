# Generated by Django 3.1.5 on 2021-02-01 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_order.job_set+', to='contenttypes.contenttype')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='TransactionJob',
            fields=[
                ('job_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='order.job')),
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('SATISFIED', 'SATISFIED'), ('FAILED', 'FAILED')], default='PENDING', max_length=10)),
                ('payment_data', models.JSONField()),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.order')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('order.job',),
        ),
    ]
