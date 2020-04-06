from django.urls import path, re_path

from .views import (
    ProductListView, ProductDetailView,
)

urlpatterns = [
    path('', ProductListView.as_view()),
    path('<slug:slug>/', ProductDetailView.as_view()),
]