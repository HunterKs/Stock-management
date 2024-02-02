# Generated by Django 4.2.2 on 2023-07-19 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_alter_order_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='size_depth',
            new_name='size',
        ),
        migrations.AlterUniqueTogether(
            name='tyre',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='order',
            name='size_length',
        ),
        migrations.RemoveField(
            model_name='order',
            name='size_width',
        ),
        migrations.AddField(
            model_name='tyre',
            name='size',
            field=models.IntegerField(default=53),
        ),
        migrations.AlterUniqueTogether(
            name='tyre',
            unique_together={('name', 'size')},
        ),
        migrations.RemoveField(
            model_name='tyre',
            name='size_depth',
        ),
        migrations.RemoveField(
            model_name='tyre',
            name='size_length',
        ),
        migrations.RemoveField(
            model_name='tyre',
            name='size_width',
        ),
    ]
