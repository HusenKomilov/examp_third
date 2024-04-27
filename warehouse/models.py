from django.db import models
from utils.models import BaseModel


class Product(BaseModel):
    title = models.CharField(max_length=128)
    code = models.CharField(max_length=64)

    @classmethod
    def calculate_dress(self, quantity):
        a = quantity * 0.8
        b = quantity * 5
        c = quantity * 10

        return {"mato": a, "tugma": b, "ip": c}

    def __str__(self):
        return self.title


class Materials(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class ProductMaterials(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product")
    material = models.ForeignKey(Materials, on_delete=models.CASCADE, related_name="material")
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.product.title}-{self.material.title}"


class Warehouses(BaseModel):
    material = models.ForeignKey(Materials, on_delete=models.CASCADE)
    remainder = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    @property
    def total_price(self):
        return self.price * self.remainder

    def __str__(self):
        return self.material.title
