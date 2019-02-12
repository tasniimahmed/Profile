from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Image = models.ImageField(max_length= 40)
    Fullname = models.CharField(max_length= 40)
    Email = models.CharField(max_length= 40)
    mobile = models.CharField(max_length= 40)
    date_of_birth = models.DateField(max_length= 40)
    address = models.CharField(max_length= 40)
    university = models.CharField(max_length= 40)
    faculty = models.CharField(max_length= 40)
    department= models.CharField(max_length= 40)
    graduation_year=models.CharField(max_length=4)
    college_id=models.CharField(max_length= 40)
    emergency_contact_name = models.CharField(max_length= 40)
    emergency_contact_number = models.CharField(max_length= 40)
    emergency_contact_relation = models.CharField(max_length= 40)
    national_id = models.CharField(max_length= 40)
    passport_id = models.CharField(max_length= 40)

    def __str__(self):
        return self.user
