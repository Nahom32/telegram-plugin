from django.db import models

# Create your models here.
class Message(models.Model):
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)
    receiver = models.CharField(max_length=255)
    
    
