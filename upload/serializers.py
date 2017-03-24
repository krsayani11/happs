from rest_framework import serializers
from .models import fileupload

class FileUploadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = fileupload
        fields = ('username', 'created', 'event_id', 'datafile')
        read_only_fields = ('created', 'datafile')