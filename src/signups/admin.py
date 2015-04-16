from django.contrib import admin

# Register your models here.
from .models import UserProfile, TrainerProfile, Client

admin.site.register(UserProfile)
#admin.site.register(TrainerProfile)
#admin.site.register(Client)
