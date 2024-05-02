from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .models import Products
from .serializers import ProductsSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination



class ProductListAPIView(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = PageNumberPagination
    serializer_class = ProductsSerializer

    def get_queryset(self):
        return Products.objects.all()

    def post(self, request):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

class ProductDetailAPIView(APIView):
    
    permission_classes = [IsAuthenticated]

    def get_object(self, productsID):
        return get_object_or_404(Products, pk=productsID)

    def put(self, request, productsID):
        product = self.get_object(productsID)
        serializer = ProductsSerializer(
            product, data=request.data, partial=True) 
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    def delete(self, request, productsID):
        product = self.get_object(productsID)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class LikeAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, productsID):
        return get_object_or_404(Products, pk=productsID)
    
    def post(self, request, productsID):
        product = self.get_object(productsID)
        if product.like_users.filter(pk=request.user.pk).exists():
            product.like_users.remove(request.user)
        else:
            product.like_users.add(request.user)
        return Response(status=status.HTTP_200_OK)