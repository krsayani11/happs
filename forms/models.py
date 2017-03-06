from django.db import models
# Create your models here.

def upload_to(instance, filename):
	return 'static/images/{}'.format(filename)

class User(models.Model):
	name = models.CharField(max_length=255)
	username = models.CharField(max_length=255, primary_key=True)
	user_id = models.BigIntegerField()
	authentication_token = models.CharField(max_length=255)
	datafile = models.ImageField(('image'), blank=True, null=True, upload_to=upload_to)

	def __str__(self):
		return self.username

class attendees(models.Model):
	username = models.ForeignKey('User', on_delete=models.CASCADE)
	attendee_event = models.ForeignKey('events.UserEvents', on_delete=models.CASCADE, default=None)

	def __str__(self):
		return self.username

	