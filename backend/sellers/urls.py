from django.urls import path

from .views import SellerListView, SellerDetailView, SellerUpdateView, SellerDeleteView


urlpatterns = [
    path('sellers/', SellerListView.as_view(), name='seller-list'),
    path('sellers/<int:pk>/', SellerDetailView.as_view(), name='seller-detail'),
    path('sellers/update/<int:pk>/', SellerUpdateView.as_view(), name='seller-update'),
    path('sellers/delete/<int:pk>/', SellerDeleteView.as_view(), name='seller-delete')
]