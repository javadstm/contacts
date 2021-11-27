from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


# Create your models here.
class contact(models.Model):
    first_name = models.CharField(max_length=48, blank=True, null=False,default='none')
    last_name = models.CharField(max_length=64, blank=True, null=False, default='none')
    phone_number = models.CharField(max_length=20, unique=True, null=False, blank=True, default='none')
    email = models.EmailField(max_length=100,blank=True,null=False,default='none')
    address = models.CharField(max_length=200, blank=True, default='none')
    author = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    # avatar

    def __str__(self):
        return self.first_name + self.last_name



