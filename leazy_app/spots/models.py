from django.db import models
from travel.models import Time_Period

class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    image = models.TextField()
    description = models.TextField()

class Region(models.Model):
    region_id = models.AutoField(primary_key=True)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.TextField()
    description = models.TextField()

class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.TextField()
    description = models.TextField()

class Spot(models.Model):
    spot_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    image = models.TextField()
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)
    description = models.TextField()
    address = models.TextField()
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)


