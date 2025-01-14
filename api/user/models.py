from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class UserCustomer(AbstractUser):
    description= models.TextField(blank=True, null=True)
    className= models.TextField(blank=True, null=True)
