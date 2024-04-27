from rest_framework import generics
from warehouse import serializers
from warehouse.models import ProductMaterials, Product
from rest_framework.response import Response
from django.db.models import OuterRef, functions, Subquery, Prefetch
from django.contrib.postgres.aggregates import ArrayAgg
from django.contrib.postgres.expressions import ArraySubquery
from django_filters.rest_framework import DjangoFilterBackend


class ProductSearchCreateAPIView(generics.GenericAPIView):
    serializer_class = serializers.ProductSerializers

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data['code']
        quantity = int(serializer.validated_data['quantity'])
        print(quantity)

        try:
            product = Product.objects.get(code=code)
            return product
            # return Response(product.calculate_dress(quantity)
        except Exception as e:
            return Response({"message": "Bunaqa mahsulot yo'q"})

    def list(self, *args, **kwargs):
        pass


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializers

