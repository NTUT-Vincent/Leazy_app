from django.db import models
from travel.models import Time_Period
from users.models import User
from spots.models import Spot

class At(models.Model):
    at_id = models.AutoField(primary_key=True)
    time_period_id = models.ForeignKey(Time_Period, on_delete=models.CASCADE)
    spot_id = models.ForeignKey(Spot, on_delete=models.CASCADE)

class Visit(models.Model):
    visit_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    spot_id = models.ForeignKey(Spot, on_delete=models.CASCADE)

# Create your models here.
