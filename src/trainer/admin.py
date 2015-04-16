from django.contrib import admin

# Register your models here.

from .models import TrainerProfile, Client

admin.site.register(TrainerProfile)
admin.site.register(Client)