# Generated by Django 4.2.2 on 2023-07-13 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_tyre_company'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='tyre',
            unique_together={('name', 'size_length', 'size_width', 'size_depth')},
        ),
    ]