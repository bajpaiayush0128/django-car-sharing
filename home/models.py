from django.utils import timezone
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=1, blank=True, null=True)
    car_name = models.CharField(max_length=120)
    date_of_trip = models.DateField(default=timezone.now)
    time_of_trip = models.TimeField(default=timezone.now)
    source = models.CharField(max_length=120)
    destination = models.CharField(max_length=120)
    vacant_seats = models.IntegerField()
    # participants = models.ManyToManyField(User, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.source + " to " + self.destination


class Profile(models.Model):
    user = models.CharField(max_length=240)
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=240)
    contact_no = models.CharField(max_length=240)
    image = models.CharField(max_length=240)

    def __str__(self):
        return self.first_name[0:100]
