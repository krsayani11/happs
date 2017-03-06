from rest_framework import viewsets, status, permissions
from rest_framework.views import APIView
from rest_framework.decorators import api_view, detail_route, list_route
from rest_framework.response import Response
from .models import UserEvents
from rest_framework.generics import (
        DestroyAPIView,
        ListAPIView,
        UpdateAPIView,
        RetrieveAPIView)
from django.http import HttpResponse
from .serializers import EventSerializer
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class EventsViewSet(viewsets.ModelViewSet):
    queryset = UserEvents.objects.all()
    serializer_class = EventSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('event_name', 
            'address', 
            'date', 
            'start_time', 
            'end_time', 
            'host', 
            'description',)

    @detail_route(methods=['post'])
    def addEvent(self, request):
        serializer = EventSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def search(request):
        queryset_list = UserEvents.objects.all() 
        query = request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(event_name__icontains=query),
                    Q(date__icontains=query),
                    Q(start_time__icontains=query),
                    Q(end_time__icontains=query),
                    Q(host__icontains=query),
                    Q(description__icontains=query),
                    )
        return queryset_list

    
def event(request, pk):
    queryset = UserEvents.objects.get(pk)
    serializer = EventSerializer
    return Response(serializer.data)

def get_user(request, image_id):
    db_image = UserModel.objects.get(pk=image_id)
    image = "../" + str(db_image.datafile)
    return render(request, 'upload/show_image.html', {'image': image})

def get_event(request, image_id):
    db_image = EventModel.objects.get(pk=image_id)
    image = "../" + str(db_image.datafile)

class EventDetailAPIView(RetrieveAPIView):
    queryset = UserEvents.objects.all()
    serializer_class = EventSerializer

class EventUpdateAPIView(UpdateAPIView):
    queryset = UserEvents.objects.all()
    serializer_class = EventSerializer

class EventDestroyAPIView(DestroyAPIView):
    queryset = UserEvents.objects.all()
    serializer_class = EventSerializer

class EventListAPIView(ListAPIView):
    queryset = UserEvents.objects.all()
    serializer_class = EventSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('event_name', 
            'address', 
            'date', 
            'start_time', 
            'end_time', 
            'host', 
            'description',)


