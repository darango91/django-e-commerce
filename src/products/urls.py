from django.urls import path, re_path

from .views import (
    ProductListView, ProductDetailView,
    ProductFeaturedListView, ProductFeaturedDetailView
)

urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('products/<slug:slug>/', ProductDetailView.as_view()),
    path('featured/', ProductFeaturedListView.as_view()),
    path('featured/<int:pk>/', ProductFeaturedDetailView.as_view()),
]