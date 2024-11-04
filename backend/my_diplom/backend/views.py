from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from my_diplom.backend.models import Product, Shop
from my_diplom.backend.serializers import ProductSerializer


class ProductView(APIView):
    def get(request, *args, **kwargs):
        shop = Shop.objects.create(name='Svyaznoy', state=True)
        Product.objects.create(name='iphone',
                               category='phones',
                               quantity=20,
                               price=80000,
                               shop=shop)
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


