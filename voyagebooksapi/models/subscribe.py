from django.db import models
from .user import User

class Subscribe(models.Model):
    
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriber')
    subscribed = models.ForeignKey(User, related_name='subscribed', on_delete=models.CASCADE)
    