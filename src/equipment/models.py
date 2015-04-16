from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode

# Create your models here.

class Equipment(models.Model):
	name = models.CharField(max_length=30)
	brand = models.CharField(max_length=30, blank=True)
	condition = models.CharField(max_length=140)
	purchase_date = models.DateField()
	happiness_rating = models.IntegerField(blank=True)
