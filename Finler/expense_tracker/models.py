from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class expense(models.Model):
	username = models.CharField(max_length=128,null=True )
	name = models.CharField(max_length=30)
	cost = models.FloatField()
	date = models.DateTimeField(auto_now=True)


