from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from .models import Seller
from .serializers import SellerSerializer


class SellerTest(TestCase):
    def setUp(self):
        self.url = reverse('seller-list')
        self.seller1 = Seller.objects.create(
            name='Seller 01',
            email='seller01@gmail.com',
            phone='45111111111'
        )
        self.seller2 = Seller.objects.create(
            name='Seller 02',
            email='seller02@gmail.com',
            phone='45222222222'
        )

    def test_create_seller(self):
        seller = Seller.objects.create(
            name='Seller 03',
            email='seller03@gmail.com',
            phone='45333333333'
        )
        self.assertEqual(seller.name, 'Seller 03')
        self.assertEqual(seller.email, 'seller03@gmail.com')
        self.assertEqual(seller.phone, '45333333333')

    def test_list_sellers(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2) 

    def test_get_seller(self):
        filter_url = f'{self.url}1/'
        response = self.client.get(filter_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Seller 01')

    def test_get_nonexistent_seller(self):
        filter_url = f'{self.url}99/'
        response = self.client.get(filter_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['message'], 'Seller not found')

    def test_update_seller(self):
        updated_data = {
            "name": "Seller Updated 01",
        }
        
        response = self.client.put(f'/api/sellers/update/{self.seller1.id}/', updated_data, format='json', content_type='application/json')
        seller = Seller.objects.get(pk=self.seller1.id)
        serializer = SellerSerializer(seller)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(seller.name, "Seller Updated 01")

    def test_update_nonexistent_seller(self):
        data = {
            "name": "NonExistentSeller",
        }

        response = self.client.put('/api/sellers/update/99/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {"message": "Seller not found"})

    def test_delete_seller(self):
        filter_url = f'{self.url}delete/1/'
        response = self.client.delete(filter_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data['message'], 'Seller deleted')

    def test_delete_nonexistent_seller(self):
        filter_url = f'{self.url}delete/99/'
        response = self.client.delete(filter_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['message'], 'Seller not found')