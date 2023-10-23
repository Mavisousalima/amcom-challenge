from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from .models import Client
from .serializers import ClientSerializer


class ClientTest(TestCase):
    def setUp(self):
        self.url = reverse('client-list')
        self.client1 = Client.objects.create(
            name='Client 01',
            email='client01@gmail.com',
            phone='63111111111'
        )
        self.client2 = Client.objects.create(
            name='Client 02',
            email='client02@gmail.com',
            phone='63222222222'
        )

    def test_create_client(self):
        client = Client.objects.create(
            name='Client 03',
            email='client03@gmail.com',
            phone='63333333333'
        )
        self.assertEqual(client.name, 'Client 03')
        self.assertEqual(client.email, 'client03@gmail.com')
        self.assertEqual(client.phone, '63333333333')

    def test_list_clients(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2) 

    def test_get_client(self):
        filter_url = f'{self.url}1/'
        response = self.client.get(filter_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Client 01')

    def test_get_nonexistent_client(self):
        filter_url = f'{self.url}99/'
        response = self.client.get(filter_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['message'], 'Client not found')

    def test_update_client(self):
        updated_data = {
            "name": "Client Updated 01",
        }
        
        response = self.client.put(f'/api/clients/update/{self.client1.id}/', updated_data, format='json', content_type='application/json')
        client = Client.objects.get(pk=self.client1.id)
        serializer = ClientSerializer(client)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(client.name, "Client Updated 01")

    def test_update_nonexistent_client(self):
        data = {
            "name": "NonExistentClient",
        }

        response = self.client.put('/api/clients/update/99/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {"message": "Client not found"})

    def test_delete_client(self):
        filter_url = f'{self.url}delete/1/'
        response = self.client.delete(filter_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data['message'], 'Client deleted')

    def test_delete_nonexistent_client(self):
        filter_url = f'{self.url}delete/99/'
        response = self.client.delete(filter_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['message'], 'Client not found')