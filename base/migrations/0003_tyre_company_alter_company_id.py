# Generated by Django 4.2.2 on 2023-07-08 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='tyre',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.company'),
        ),
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
