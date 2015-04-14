from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode

# Create your models here.

class SignUp(models.Model):
	first_name = models.CharField(max_length=120) #defaults to null=False, blank=False
	last_name = models.CharField(max_length=120) #defaults to null=False, blank=False
	username = models.CharField(max_length=30, null=False, blank=False) 
	email = models.EmailField() #defaults to null=False, blank=False

	password = models.CharField(max_length=50)
	
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	CLIENT = 'CL'
	TRAINER = 'TR'
	EMPLOYEE = 'EM'

	USER_TYPE_CHOICE = (
			(CLIENT, 'Client'),
			(TRAINER, 'Trainer'),
			(EMPLOYEE, 'Employee'),
		)

	user_type = models.CharField(max_length=2,

		choices = USER_TYPE_CHOICE,

		default=CLIENT)

	def __unicode__(self):
		return smart_unicode(self.email)

class UserProfile(models.Model):
	# Links UserProfile to a User model instance
	user = models.OneToOneField(User)

	#additional attributes
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)

	def __unicode__(self):
		return self.user.username

