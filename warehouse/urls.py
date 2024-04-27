from django.urls import path
from .views import ProductListAPIView, ProductSearchCreateAPIView

urlpatterns = [
    path("", ProductSearchCreateAPIView.as_view()),
]
