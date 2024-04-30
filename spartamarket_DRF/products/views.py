from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Products
from .serializers import ProductsSerializer
from django.shortcuts import get_object_or_404

class ProductListAPIView(APIView):
    
    def get(self, request):
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)