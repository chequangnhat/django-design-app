# Create your models here.
from django.db import models

from django.contrib.auth.models import User
    
class Design(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    design = models.TextField()
