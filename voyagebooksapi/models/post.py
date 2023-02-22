from django.db import models
from .user import User

class Post(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=55)
    location = models.CharField(max_length=55)
    photo_url = models.CharField(max_length=255)
    content = models.TextField(max_length=1000)
    creation_date = models.DateField()
    
    def __str__(self):
        return self.name
