from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    full_name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username