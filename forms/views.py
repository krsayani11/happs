from django.shortcuts import render
from django.http import HttpResponse
from .models import user, attendees
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, AttendeesSerializer
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import api_view, detail_route, list_route
from rest_framework import generics
from django.db.models import Q
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
        DestroyAPIView,
        ListAPIView,
        UpdateAPIView,
        RetrieveAPIView)


class UserViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name','username', 'user_id', 'authentication_token', 'friends')
    @detail_route(methods=['post'])
    def addUser(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserUpdateAPIView(UpdateAPIView):
    queryset = user.objects.all()
    serializer_class = UserSerializer
    lookup_fields = ('user_id')

def search(request):
    queryset_list = user.objects.all() 
    query = self.request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
                Q(username__icontains=query))
    return queryset_list

class AttendeesViewSet(viewsets.ModelViewSet):
    queryset = attendees.objects.all()
    serializer_class = AttendeesSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('username','attendee_event',)
    @detail_route(methods=['post'])
    def updateUser(self, request):
        serializer = AttendeesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AttendeesDestroyAPIView(DestroyAPIView):
    queryset = attendees.objects.all()
    serializer_class = AttendeesSerializer
