from rest_framework import serializers
from warehouse import models


class MaterialSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Materials
        fields = ("pk", "title",)


class ProductMaterialSerializers(serializers.ModelSerializer):
    material = MaterialSerializers()

    class Meta:
        model = models.ProductMaterials
        fields = ("pk", "material", "quantity")


class WarehouseSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Warehouses
        fields = ("pk", "material", "remainder", "price", "total_price")


class ProductSerializers(serializers.ModelSerializer):
    quantity = serializers.IntegerField(default=0)

    # product_materials = serializers.ListSerializer(child=ProductMaterialSerializers(), source="product")
    # product_materials = WarehouseSerializers()

    class Meta:
        model = models.Product
        fields = ("code", "quantity", "calculate_dress")

