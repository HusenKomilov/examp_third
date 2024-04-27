from django.contrib import admin
from warehouse import models

admin.site.register(models.Product)
admin.site.register(models.Materials)
admin.site.register(models.ProductMaterials)
admin.site.register(models.Warehouses)
