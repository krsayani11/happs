from rest_framework import serializers
from .models import User, attendees

class AttendeesSerializer(serializers.ModelSerializer):
	class Meta:
		model = attendees
		fields = ('username', 'attendee_event',)

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('name', 'username', 'user_id', 'authentication_token', 'datafile')
		read_only_fields = ('datafile',)
