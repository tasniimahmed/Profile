from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    fullname = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    mobile = models.CharField(max_length=30)
    birthdate = models.DateField(max_length=30)
    address = models.CharField(max_length=30)
    university = models.CharField(max_length=30)
    faculty = models.CharField(max_length=30)
    collegedepartment= models.CharField(max_length=30)
    ExpectedYearOfGraduation = models.CharField(max_length=4)
    CollegeID = models.CharField(max_length=30)
    EmergencyContactRelation = models.CharField(max_length=7)
    NationalID = models.CharField(max_length=30)
    PassportID = models.CharField(max_length=30)
    


    
    def __str__(self):
        return self.user
      ##  return f'{self.user.username} Profile'
