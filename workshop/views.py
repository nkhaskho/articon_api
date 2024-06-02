from django.shortcuts import render
from django.http import Http404
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .models import Workshop
from .serializers import WorkshopSerializer

# List and create workshops
class WorkshopList(generics.ListCreateAPIView):
 
    queryset = Workshop.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('title', 'date') 
    search_fields = ('title', 'description')  
    serializer_class = WorkshopSerializer

# Retrieve, update, or delete a  workshop
class WorkshopDetail(APIView):
 
    # permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Workshop.objects.get(pk=pk)
        except Workshop.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        workshop = self.get_object(pk)
        serializer = WorkshopSerializer(workshop)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        workshop = self.get_object(pk)
        serializer = WorkshopSerializer(workshop, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        workshop = self.get_object(pk)
        workshop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
