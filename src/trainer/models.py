from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode


# Create your models here.

class TrainerProfile(models.Model):
	trainer = models.OneToOneField(User)
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)
	def __unicode__(self):
		return self.trainer.username
	#need access to equipment


class Client(models.Model):
	client = models.OneToOneField(User, default=1)
	trainerID = models.ForeignKey(TrainerProfile)
