# tests/test_models.py
from django.test import TestCase
from .models import Destination
from rest_framework.test import APITestCase
from rest_framework import status






class DestinationModelTestCase(TestCase):
    def test_destination_fields(self):
        destination = Destination.objects.create(
            name='Paris',
            country='France',
            description='City of Love',
            best_time_to_visit='Spring',
            category='City',
            image_url='https://example.com/paris.jpg'
        )
        self.assertEqual(destination.name, 'Paris')
        self.assertEqual(destination.country, 'France')
        self.assertEqual(destination.description, 'City of Love')
        self.assertEqual(destination.best_time_to_visit, 'Spring')
        self.assertEqual(destination.category, 'City')
        self.assertEqual(destination.image_url, 'https://example.com/paris.jpg')

    def test_destination_str_representation(self):
        destination = Destination.objects.create(name='Paris')
        self.assertEqual(str(destination), 'Paris')

from rest_framework.test import APITestCase
from rest_framework import status
from .models import Destination
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import User

class DestinationAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = AccessToken.for_user(self.user)
        self.destination = Destination.objects.create(
            name='Paris',
            country='France',
            description='City of Love',
            best_time_to_visit='Spring',
            category='City',
            image_url='https://example.com/paris.jpg'
        )

    def test_get_destination_list(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token))
        response = self.client.get('/a1/travel/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Paris')

    def test_create_destination(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token))
        data = {
            'name': 'London',
            'country': 'UK',
            'description': 'Capital city of the UK',
            'best_time_to_visit': 'Summer',
            'category': 'City',
            'image_url': 'https://example.com/london.jpg'
        }
        print("Request Data:", data)  # Debugging: Print the request data
        response = self.client.post('/a1/travel/', data, format='json')
        print("Response Data:", response.data)  # Debugging: Print the response data
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Destination.objects.count(), 2)

    # Write similar tests for other CRUD operations (update, delete)

'''
class DestinationAPITestCase(APITestCase):
    def setUp(self):
        self.destination = Destination.objects.create(
            name='Paris',
            country='France',
            description='City of Love',
            best_time_to_visit='Spring',
            category='City',
            image_url='https://example.com/paris.jpg'
        )

    def test_get_destination_list(self):
        response = self.client.get('/a1/travel/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Paris')

    def test_create_destination(self):
        data = {
            'name': 'London',
            'country': 'UK',
            'description': 'Capital city of the UK',
            'best_time_to_visit': 'Summer',
            'category': 'City',
            'image_url': 'https://example.com/london.jpg'
        }
        response = self.client.post('/a1/travel/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Destination.objects.count(), 2)

    # Write similar tests for other CRUD operations (update, delete)

'''
'''
class DestinationModelTestCase(TestCase):
    def test_destination_fields(self):
        destination = Destination.objects.create(
            name='Paris',
            country='France',
            description='City of Love',
            best_time_to_visit='winter',
            
        )
        self.assertEqual(destination.name, 'Paris')
        self.assertEqual(destination.country, 'France')
        self.assertEqual(destination.description, 'City of Love')
        self.assertEqual(destination.best_time_to_visit, 'winter')

    def test_destination_name_max_length(self):
        max_length = Destination._meta.get_field('name').max_length
        self.assertEqual(max_length, 30)

    def test_destination_country_max_length(self):
        max_length = Destination._meta.get_field('country').max_length
        self.assertEqual(max_length, 30)


    def test_destination_best_time_to_visit_max_length(self):
        max_length = Destination._meta.get_field('best_time_to_visit').max_length
        self.assertEqual(max_length, 40)

'''
