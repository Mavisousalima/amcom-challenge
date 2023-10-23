from django.urls import path

from .views import SaleListView, SaleDetailView, SaleUpdateView, SaleDeleteView, SaleCreateView

urlpatterns = [
    path('sales/', SaleListView.as_view(), name='sale-list'),
    path('sales/<int:pk>/', SaleDetailView.as_view(), name='sale-detail'),
    path('sales/add/', SaleCreateView.as_view(), name='sale-add'),
    path('sales/update/<int:pk>/', SaleUpdateView.as_view(), name='sale-update'),
    path('sales/delete/<int:pk>/', SaleDeleteView.as_view(), name='sale-delete')
]