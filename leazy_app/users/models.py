from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator, MinLengthValidator, \
    MaxLengthValidator
from django.db import models

def genderValidator(value):
    if value not in ['F', 'M']:
        raise ValidationError(
            'Gender column only can be "M" or "F".'
        )

class User(models.Model):
    alphanumericValidator = RegexValidator(r'^[0-9a-zA-Z_]*$', 'Only alphanumeric characters are allowed.')

    user_id = models.CharField(
        max_length=22, primary_key=True, validators=[MinLengthValidator(3), alphanumericValidator])
    gender = models.CharField(max_length=1, validators=[genderValidator])
    first_name = models.CharField(max_length=30, validators=[MinLengthValidator(1), alphanumericValidator])
    first_name = models.CharField(max_length=30, validators=[MinLengthValidator(1), alphanumericValidator])
    password = models.CharField(
        max_length=16, validators=[MinLengthValidator(8), alphanumericValidator])
    age = models.IntegerField(validators=[MinValueValidator(0)])

# Create your models here.
