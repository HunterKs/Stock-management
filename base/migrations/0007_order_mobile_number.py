# Generated by Django 4.2.2 on 2023-07-13 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_order_customer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='mobile_number',
            field=models.CharField(default=0, max_length=10),
        ),
    ]