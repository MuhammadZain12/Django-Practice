from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
  
  # One to one relationship to extend official User model
  
  user=models.OneToOneField(User,on_delete=models.CASCADE)

  # For extra attributes for which we extended the main model

  portfolio=models.URLField(blank=TRUE)
  profile_image=models.ImageField(upload_to='profile_pic',blank=TRUE)

  def __str__(self) -> str:
    return self.user.username

