# Generated by Django 4.2.2 on 2023-07-19 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_alter_order_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tyre',
            name='size',
            field=models.TextField(default=0.15104166666666666),
        ),
    ]