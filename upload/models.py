from __future__ import unicode_literals
from django.db import models
from forms.models import user

def upload_to(instance, filename):
	return 'static/images/{}'.format(filename)

class fileupload(models.Model):
	username = models.ForeignKey(
         'forms.user',
         on_delete=models.CASCADE,
         default = None,)
	created = models.DateTimeField(auto_now_add=True)
	event_id = models.IntegerField()
	datafile = models.ImageField(('image'), blank=True, null=True, upload_to=upload_to)