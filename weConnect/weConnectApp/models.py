from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, primary_key = True,on_delete=models.CASCADE)
    name = models.CharField(max_length =30, blank = True, null = True)
    about = models.TextField(max_length = 200, blank=True)
    profilePic = models.ImageField(upload_to='profilePic', default=None)
    DOB = models.DateField()