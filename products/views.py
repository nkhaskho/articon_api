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

class CategoryList(generics.ListCreateAPIView):
    """
    List all Categories, or create a new Category.
    """
    queryset = Category.objects.filter()
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('type', 'status')
    serializer_class = CategorySerializer


class CategoryDetail(APIView):
    """
    Retrieve, update or delete a Category.
    """
    #permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductList(generics.ListCreateAPIView):
    """
    List all Products, or create a new Product.
    """
    queryset = Product.objects.filter()
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('category', 'price')
    serializer_class = ProductSerializer


class ProductDetail(APIView):
    """
    Retrieve, update or delete a Product.
    """
    #permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class ReviewList(generics.ListCreateAPIView):
    """
    List Reviews of a given Product.
    """
    queryset = Review.objects.filter()
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('product')
    serializer_class = ReviewSerializer


class ReviewDetail(APIView):
    """
    Retrieve, update or delete a Review.
    """
    #permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        review = self.get_object(pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



