from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class profile(models.Model):
    User=models.OneToOneField(User,on_delete=models.CASCADE)
    follows=models.ManyToManyField("self",
        related_name="followed_by",
        symmetrical=False,
        blank=True)
    
    def __str__(self):
        return self.User.username
    
def create_profile(sender,instance,created,**kwargs):    
    
