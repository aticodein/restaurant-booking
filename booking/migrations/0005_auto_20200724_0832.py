# Generated by Django 3.0.8 on 2020-07-24 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20200724_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingitem',
            name='time',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]