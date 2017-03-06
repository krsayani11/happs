from __future__ import unicode_literals
from django.db import models
from forms.models import User

def upload_to(instance, filename):
	return 'static/images/{}'.format(filename)

class FileUpload(models.Model):
	username = models.ForeignKey(
         'forms.User',
         on_delete=models.CASCADE,
         default = None,)
	created = models.DateTimeField(auto_now_add=True)
	event_id = models.IntegerField()
	datafile = models.ImageField(('image'), blank=True, null=True, upload_to=upload_to)