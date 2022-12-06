from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Book(models.Model):
    created= models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField()
    # cover = models.ImageField(upload_to='',null=True)
    
    def __str__(self):
        return self.title

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    first_name = models.CharField(max_length=200 , null=True ,blank=True)
    last_name = models.CharField(max_length=200 , null=True ,blank=True)
    email = models.EmailField(max_length=200,blank=True ,null=True)

    def __str__(self):
        return str(self.user)