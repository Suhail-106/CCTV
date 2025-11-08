from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone  

class ImageURL(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url
    
class contactinfo(models.Model):
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    address = models.TextField()
    massage = models.TextField()
    selectcategory = models.CharField(
        max_length=50,default="working",
        choices=[
            ('working','Working'),
            ('installing','Installing'),
            ('servicing','Servicing')
        ]
    )
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.selectcategory}"    
    



class CCTVElectrical(models.Model):
    name = models.CharField(max_length=100)
    imageurl = models.URLField(max_length=200)

    def __str__(self):
        return self.name
    

class datasave(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    gender = models.CharField(
        max_length=50,default="select gender",
        choices=[
            ('male','Male'),
            ('female','Female'),
            ('other','Other')
        ]
    )
    password = models.CharField(max_length=50)
    user_otp = models.CharField(max_length=6, blank=True, default='000000')
    confirmpassword = models.CharField(max_length=50)
    session_otp = models.CharField(max_length=6, blank=True, default='000000')
    DOB = models.DateField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)  # Image field add kiya

    

    def __str__(self):
        return self.username


