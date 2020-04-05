from django.urls import path

from .views import ProductListView
from .views import ProductDetailView

urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('products/<int:pk>/', ProductDetailView.as_view()),
]