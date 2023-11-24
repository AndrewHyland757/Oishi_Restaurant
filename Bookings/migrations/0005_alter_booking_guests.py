# Generated by Django 3.2.3 on 2023-11-24 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookings', '0004_alter_booking_guests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='guests',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')], default=1),
        ),
    ]
