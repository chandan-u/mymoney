from django.db import models
from django.contrib.auth.models import User
from mymoney.apps.Sources.models import Source
# Create your models here.

class Credit(models.Model):

    to = models.charField(max_lenght=50)
    amount = models.IntegerField()
    status = models.CharField(max_length=6, choices)   # open/closed choices
    deductFromSource = models.ForeignKey(Source, blank=True, null=True)
    user = models.ForeignKey.(User)
    issued_date = models.DateField()
    expected_clearance_date = models.DateField()




   
    
