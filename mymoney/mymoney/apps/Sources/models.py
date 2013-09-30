from django.db import models
from django.auth.contrib.models import User

from datetime import date
# Create your models here.


class Source(models.Model):

    user =   models.ForeignKey(User, unique=True)
    title =  models.CharField(max_length=50)
    details = models.CharField(max_length=150)
    current_balance = models.IntegerField() 
    startDate = models.DateField(_("Date"), default=date.today) 
    type = models.CharField(max_length=2, choices)
    lock_date = models.DateFiled()



