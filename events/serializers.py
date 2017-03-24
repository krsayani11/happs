from .models import userevents
from forms.models import user
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        fields = self.context['request'].query_params.get('fields')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class EventSerializer(serializers.HyperlinkedModelSerializer, DynamicFieldsModelSerializer):
    class Meta:
        model = userevents
        fields = (
            'id',
            'event_name', 
            'address', 
            'date', 
            'start_time', 
            'end_time', 
             'host', 
            'description',
            'longitude',
            'latitude',
            'datafile',)
        read_only_fields = ('datafile',)