from django.urls import path

from products.views import ProductListView, ProductDetailView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<str:code>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/update/<str:code>/', ProductUpdateView.as_view(), name='product-update'),
    path('products/delete/<str:code>/', ProductDeleteView.as_view(), name='product-delete')
]