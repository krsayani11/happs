from rest_framework import serializers
from .models import Picture

class MediaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Picture
		fields = ('name', 'city', 'state', 'date', 'time')