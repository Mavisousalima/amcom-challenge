from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from .models import Product
from .serializers import ProductSerializer


class ProductTest(TestCase):
    def setUp(self):
        self.url = reverse('product-list')
        self.product1 = Product.objects.create(
            code='P001',
            description='Product 01',
            unit_price=10.0,
            commission_rate=0.05
        )
        self.product2 = Product.objects.create(
            code='P002',
            description='Product 02',
            unit_price=20.0,
            commission_rate=0.05
        )

    def test_code(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('code').verbose_name
        self.assertEqual(field_label, 'code')

    def test_description(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_unit_price(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('unit_price').verbose_name
        self.assertEqual(field_label, 'unit price')

    def test_commission_rate(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('commission_rate').verbose_name
        self.assertEqual(field_label, 'commission rate')

    def test_code_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('code').max_length
        self.assertEqual(max_length, 10)

    def test_description_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('description').max_length
        self.assertEqual(max_length, 100)

    def test_unit_price_decimal_places(self):
        product = Product.objects.get(id=1)
        decimal_places = product._meta.get_field('unit_price').decimal_places
        self.assertEqual(decimal_places, 2)

    def test_commission_rate_decimal_places(self):
        product = Product.objects.get(id=1)
        decimal_places = product._meta.get_field('commission_rate').decimal_places
        self.assertEqual(decimal_places, 2)

    def test_product_str_method(self):
        product = Product.objects.get(id=1)
        self.assertEqual(str(product), 'Product 01')

    def test_create_product(self):
        product = Product.objects.create(
            code='P003',
            description='Product 03',
            unit_price=15.0,
            commission_rate=0.08
        )
        self.assertEqual(product.code, 'P003')
        self.assertEqual(product.description, 'Product 03')
        self.assertEqual(product.unit_price, 15.0)
        self.assertEqual(product.commission_rate, 0.08)

    def test_list_products(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2) 

    def test_get_product_by_code(self):
        filter_url = f'{self.url}P001/'
        response = self.client.get(filter_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['code'], 'P001')

    def test_get_nonexistent_product(self):
        filter_url = f'{self.url}X009/'
        response = self.client.get(filter_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['message'], 'Product not found')

    def test_update_product(self):
        updated_data = {
            "code": "P001",
            "description": "Updated Product",
        }
        
        response = self.client.put(f'/api/products/update/{self.product1.code}/', updated_data, format='json', content_type='application/json')
        product = Product.objects.get(code=self.product1.code)
        serializer = ProductSerializer(product)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(product.description, "Updated Product")

    def test_update_nonexistent_product(self):
        data = {
            "code": "NonExistentCode",
            "description": "Updated Product",
        }

        response = self.client.put('/api/products/update/NonExistentCode/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {"message": "Product not found"})

    def test_delete_product(self):
        filter_url = f'{self.url}delete/P001/'
        response = self.client.delete(filter_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data['message'], 'Product deleted')

    def test_delete_nonexistent_product(self):
        filter_url = f'{self.url}delete/X009/'
        response = self.client.delete(filter_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['message'], 'Product not found')