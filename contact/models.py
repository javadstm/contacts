from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


# Create your models here.
class contact(models.Model):
    first_name = models.CharField(max_length=48, blank=False, null=False)
    last_name = models.CharField(max_length=64, blank=False, null=False)
    phone_number = models.CharField(max_length=20, unique=True, null=False, blank=False)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=200, blank=True)

    # author = models.ManyToManyField(User)
    # avatar

    def __str__(self):
        return self.first_name + self.last_name
