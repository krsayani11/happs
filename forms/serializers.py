from rest_framework import serializers
from .models import user, attendees

class AttendeesSerializer(serializers.ModelSerializer):
	class Meta:
		model = attendees
		fields = ('username', 'attendee_event',)

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = user
		fields = ('name', 'username', 'user_id', 'authentication_token', 'datafile', 'friends')
		read_only_fields = ('datafile',)
