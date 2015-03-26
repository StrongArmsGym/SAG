from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.

class SignUp(models.Model):
	first_name = models.CharField(max_length=120) #defaults to null=False, blank=False
	last_name = models.CharField(max_length=120) #defaults to null=False, blank=False
	email = models.EmailField() #defaults to null=False, blank=False

	password = models.CharField(max_length=50)
	
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return smart_unicode(self.email)
