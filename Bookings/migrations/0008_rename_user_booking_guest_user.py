# Generated by Django 3.2.3 on 2023-11-25 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bookings', '0007_auto_20231125_1805'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='user',
            new_name='guest_user',
        ),
    ]
