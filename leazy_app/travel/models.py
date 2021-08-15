from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator, MinLengthValidator, \
    MaxLengthValidator
from django.db import models
from users.models import User
from spots.models import Spot

def genderValidator(value):
    if value not in ['F', 'M']:
        raise ValidationError(
            'Gender column only can be "M" or "F".'
        )

class Trip(models.Model):
    trip_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='traveler')

class Day(models.Model):
    day_id = models.AutoField(primary_key=True)
    date = models.DateField()
    trip_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="included")

class Time_Period(models.Model):
    time_period_id = models.AutoField(primary_key=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    spot_id = models.ForeignKey(Spot, on_delete=models.CASCADE)

class Visit(models.Model):
    visit_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    spot_id = models.ForeignKey(Spot, on_delete=models.CASCADE)


# Create your models here.
