from django.db import models

# Create your models here.

class Book(models.Model):
    created= models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField()
    # cover = models.ImageField(upload_to='',null=True)
    
    def __str__(self):
        return self.title