from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode

# Create your models here.

class UserProfile(models.Model):
	# Links UserProfile to a User model instance
	user = models.OneToOneField(User)

	#additional attributes
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)
	is_trainer = models.BooleanField(default=False, editable=False)
	def __unicode__(self):
		return self.user.username

		


	
