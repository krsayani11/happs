from django.contrib import admin
from .models import User, attendees
# Register your models here.
admin.site.register(User)
admin.site.register(attendees)