from django.shortcuts import render
from django.http import HttpResponse
from .models import Picture
from rest_framework.response import Response
from .serializers import MediaSerializer
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import api_view, detail_route, list_route
from django_filters.rest_framework import DjangoFilterBackend

def index(request):
    return HttpResponse("<h1>This is the forms homepage</h1>")


class MediaViewSet(viewsets.ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = MediaSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = (
            'name', 
            'city', 
            'state', 
            'date', 
            'time', )

    @detail_route(methods=['post'])
    def addPicture(self, request):
        serializer = MediaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)