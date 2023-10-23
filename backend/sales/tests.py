from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from .models import Sale, SaleItem
from clients.models import Client
from products.models import Product
from sellers.models import Seller


class SaleTest(TestCase):
    def setUp(self):
        self.url = reverse('sale-list')
        self.client1 = Client.objects.create(name='Test Client 01', email='client01@gmail.com', phone='1234567890')
        self.seller = Seller.objects.create(name='Test Seller 01', email='seller01@gmail.com', phone='9876543210')
        self.product = Product.objects.create(code='P001', description='Sample Product', unit_price=10.0, commission_rate=0.05)
        self.sale_data = {
            'invoice_number': 'INV001',
            'date_time': '2023-10-21T12:00:00Z',
            'client': self.client1,
            'seller': self.seller,
        }
        self.sale = Sale.objects.create(**self.sale_data)
        self.sale_item = SaleItem.objects.create(sale=self.sale, product=self.product, quantity_sold=10)
        self.sale.products.add(self.product)

    def test_create_sale(self):
        response = self.client.post(self.url + 'add/', {
            'invoice_number': 'INV002',
            'date_time': '2023-10-22T12:00:00Z',
            'client': self.client1.id,
            'seller': self.seller.id,
            'products': [self.product.id],
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Sale.objects.count(), 2)

    def test_get_sale(self):
        response = self.client.get(f'/api/sales/{self.sale.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_sale(self):
        updated_data = {
            'invoice_number': 'INV003',
            'date_time': '2023-10-23T12:00:00Z',
            'client': self.client1.id,
            'seller': self.seller.id,
            'products': [self.product.id],
        }
        response = self.client.put(f'/api/sales/update/{self.sale.id}/', updated_data, format='json', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.sale.refresh_from_db()
        self.assertEqual(self.sale.invoice_number, 'INV003')

    def test_delete_sale(self):
        response = self.client.delete(f'/api/sales/delete/{self.sale.id}/', format='json', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Sale.objects.count(), 0)