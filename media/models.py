from __future__ import unicode_literals

from django.db import models

class picture(models.Model):
	name = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=255)
	date = models.DateField(auto_now_add=True)
	time = models.TimeField(auto_now_add=True)

	def __str__(self):
		return self.name