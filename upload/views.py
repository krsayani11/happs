from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.http import HttpResponse
from django.shortcuts import render
from .models import fileupload
from .serializers import FileUploadSerializer
from django.utils.encoding import smart_str
from PIL import Image
from django_filters.rest_framework import DjangoFilterBackend

def get_image(request, image_id):
    db_image = fileupload.objects.get(pk=image_id)
    image = "../" + str(db_image.datafile)
    return render(request, 'upload/show_image.html', {'image': image})

class FileUploadViewSet(ModelViewSet):
    
    queryset = fileupload.objects.all()
    serializer_class = FileUploadSerializer
    parser_classes = (MultiPartParser, FormParser,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = (
            'username', 
            'created', 
            'event_id',)
    def perform_create(self, serializer):
        serializer.save(datafile=self.request.data.get('datafile'))

    def retrieve(self, request, pk, format=""):
        images = []
        db_image = fileupload.objects.filter(username=pk)
        for each in db_image:
            images.append(str(each.datafile))
        return render(request, 'upload/show_image.html', {'images': images, 'username': pk})
