from django.urls import path

from .views import ClientListView, ClientDetailView, ClientUpdateView, ClientDeleteView


urlpatterns = [
    path('clients/', ClientListView.as_view(), name='client-list'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('clients/update/<int:pk>/', ClientUpdateView.as_view(), name='client-update'),
    path('clients/delete/<int:pk>/', ClientDeleteView.as_view(), name='client-delete')
]