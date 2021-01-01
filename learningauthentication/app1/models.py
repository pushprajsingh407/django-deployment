from django.db import models
from django.contrib.auth.models import User  #importing builtin model for user

# Create your models here.

class UserProfileInfo(models.Model):        #inhering class from models.Model class

    #Create relationship (dont inherit from User)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #Add any additional attribute
    portfolio_site = models.URLField(blank=True)
    profile_pics = models.ImageField(upload_to='profile_pics', blank=True)


    def __str__(self):
        return self.user.username
