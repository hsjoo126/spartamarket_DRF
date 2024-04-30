from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Products
from .serializers import ProductsSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

class ProductListAPIView(APIView):
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

class ProductDetailAPIView(APIView):
    
    def get_object(self, productsID):
        return get_object_or_404(Products, pk=productsID)

    def put(self, request, productsID):
        product = self.get_object(productsID)
        serializer = ProductsSerializer(
            product, data=request.data, partial=True)  # 원래 있던 데이터 넣어주기, 부분 설정 가능!
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    def delete(self, request, productsID):
        product = self.get_object(productsID)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)