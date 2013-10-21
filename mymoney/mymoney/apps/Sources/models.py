from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Source(models.Model):
    
    LOCKED = 'LO'
    UNLOCKED = 'UL'
    TYPE_CHOICES = (
        (LOCKED, 'Locked'),
        (UNLOCKED, 'Unlocked'),
    ) 
    user =   models.ForeignKey(User)
    title =  models.CharField(max_length=50)
    details = models.CharField(max_length=150)
    current_balance = models.IntegerField() 
    startDate = models.DateField(auto_now_add=True) 
    type = models.CharField(max_length=2, choices = TYPE_CHOICES, blank=True)
    lock_date = models.DateField()



