# Generated by Django 4.2.1 on 2023-05-16 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_profile_image_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='seats_booked',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]