# Generated by Django 4.2.1 on 2023-05-08 18:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=240)),
                ('first_name', models.CharField(max_length=240)),
                ('last_name', models.CharField(max_length=240)),
                ('contact_no', models.CharField(max_length=240)),
                ('image', models.CharField(max_length=240)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=120)),
                ('date_of_trip', models.DateField(default=django.utils.timezone.now)),
                ('time_of_trip', models.TimeField(default=django.utils.timezone.now)),
                ('source', models.CharField(max_length=120)),
                ('destination', models.CharField(max_length=120)),
                ('vacant_seats', models.IntegerField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
