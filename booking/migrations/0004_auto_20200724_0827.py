# Generated by Django 3.0.8 on 2020-07-24 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20200723_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingitem',
            name='time',
            field=models.DecimalField(decimal_places=0, max_digits=6),
        ),
    ]
