from django.contrib import admin

# Register your models here.
from .models import SignUp
from .models import UserProfile


class SignUpAdmin(admin.ModelAdmin):
	class Meta:
		model = SignUp


admin.site.register(SignUp, SignUpAdmin)
admin.site.register(UserProfile)