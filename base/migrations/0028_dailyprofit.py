# Generated by Django 4.2.2 on 2024-01-10 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0027_delete_dailyprofit'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyProfit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('daily_profit', models.IntegerField(default=0)),
                ('tyre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.tyre')),
            ],
        ),
    ]