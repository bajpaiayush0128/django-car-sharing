# Generated by Django 3.1.1 on 2022-05-09 19:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20220420_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='car_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=120),
            preserve_default=False,
        ),
    ]