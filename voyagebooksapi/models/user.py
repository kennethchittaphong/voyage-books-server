from django.db import models

class User(models.Model):
    
    uid = models.CharField(max_length=55)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    about = models.CharField(max_length=280)
    profile_image_url = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + self.last_name
