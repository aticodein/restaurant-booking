# Generated by Django 3.0.8 on 2020-07-23 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingitem',
            name='time',
            field=models.DecimalField(decimal_places=2, max_digits=2),
        ),
    ]
