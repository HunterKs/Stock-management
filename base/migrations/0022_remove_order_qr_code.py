# Generated by Django 4.2.2 on 2023-12-20 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_alter_order_qr_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='qr_code',
        ),
    ]
