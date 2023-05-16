from django.utils import timezone
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=1, blank=True, null=True)
    # riders = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    car_name = models.CharField(max_length=120)
    date_of_trip = models.DateField(default=timezone.now)
    time_of_trip = models.TimeField(default=timezone.now)
    source = models.CharField(max_length=120)
    destination = models.CharField(max_length=120)
    vacant_seats = models.IntegerField()
    price= models.FloatField(default=0)
    # participants = models.ManyToManyField(User, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.source + " to " + self.destination


class Profile(models.Model):
    user = models.CharField(max_length=240)
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=240)
    contact_no = models.CharField(max_length=240)
    email= models.EmailField(max_length=254, null=True, blank=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.first_name[0:100]
    
class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    phone=models.CharField(max_length=13)
    desc=models.TextField()
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + '-' + self.email 

# This model is savig ride information
class Booking(models.Model):
    post=models.ForeignKey("Post", on_delete=models.CASCADE)
    riders_id=models.IntegerField(blank=True, null=True)
    seats_booked=models.IntegerField(blank=True, null=True, default=0)



