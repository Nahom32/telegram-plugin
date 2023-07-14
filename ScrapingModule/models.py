from django.db import models
class Member(models.Model):
    name = models.CharField(max_length=255)
    user_name = models.CharField(unique=True, max_length=255)
    phone_number = models.CharField(unique=True,null=True, max_length=255)
    

# Create your models here.
