from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
  pass

class Client(models.Model):
      appointmentID=models.IntegerField(default=0)
      name=models.TextField()
      email=models.CharField(max_length=200)
      phone=models.IntegerField(default=0)
      subject=models.TextField()

class Appointment(models.Model):
     appointmentID=models.IntegerField(default=0)
     day=models.TextField()
     hour=models.TextField()

     def __str__(self):
        return f"{self.appointmentID} {self.day} {self.hour}"
class Visitor(models.Model):
    HOURS_CHOICES=[
        ('10AM', '10:00AM'),
        ('11AM', '11:00AM'),
        ('1PM', '1:00PM'),
        ('2PM', '2:00PM'),
        ('3PM', '3:00PM'),
        ('4PM', '4:00PM'),
        ]
    DATE_CHOICES=[
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ]
    phone=models.BigIntegerField(primary_key=True)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    subject=models.TextField()
    day=models.CharField(
        max_length=10,
        choices=DATE_CHOICES,
        default='Monday')
    hour=models.CharField(
        max_length=5,
        choices=HOURS_CHOICES,
        default='10:00AM',
        )
    class Meta:
        unique_together = ('day', 'hour',)