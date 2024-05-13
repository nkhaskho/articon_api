from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import generics

from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from django.http import Http404

from .models import *
from .serializers import *

# Create your views here.
class EventList(generics.ListCreateAPIView):
    """
    List all Categories, or create a new Event.
    """
    queryset = Event.objects.filter()
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('type')
    serializer_class = EventSerializer


class EventDetail(APIView):
    """
    Retrieve, update or delete an Event.
    """
    #permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
