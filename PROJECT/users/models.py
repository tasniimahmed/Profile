from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profilepic = models.ImageField()
    Fullname = models.CharField(max_length=50)
    Mobile = models.CharField(max_length=30)
    DOB = models.DateField(max_length=30)
    Address = models.CharField(max_length=30)
    University = models.CharField(max_length=30)
    Faculty = models.CharField(max_length=30)
    College_Department= models.CharField(max_length=30)
    Expected_Year_Of_Graduation = models.CharField(max_length=4)
    College_id = models.CharField(max_length=30)
    Em_contact_name = models.CharField(max_length=7)
    Em_contact_mobile = models.CharField(max_length=20)
    national_id = models.CharField(max_length=30)
    National_id_front = models.ImageField()
    National_id_back = models.ImageField()
    Passport_id = models.CharField(max_length=30)
    Passport_id_im = models.ImageField()
    


    
    def __str__(self):
        return self.user
      ##  return f'{self.user.username} Profile'
