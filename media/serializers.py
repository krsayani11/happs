from rest_framework import serializers
from .models import picture

class MediaSerializer(serializers.ModelSerializer):
	class Meta:
		model = picture
		fields = ('name', 'city', 'state', 'date', 'time')