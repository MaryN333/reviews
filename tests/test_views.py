from django.test import TestCase, Client
from django.urls import reverse
from restaurant.models import Type, Restaurant, Review


from django.contrib.auth.models import User
from django.utils import timezone


class ViewTestCase(TestCase):
    def test_index_loads_properly(self):
        url = reverse('restaurant:index')
        response = self.client.get(url)
        # Verifying that an API request returns status code 200
        self.assertEqual(response.status_code, 200)


class AnotherViewTestCase(TestCase):
    def setUp(self):
        # Create a Type for a Restaurant
        self.type = Type.objects.create(name='Test Type')

        # Create a Restaurant
        self.restaurant = Restaurant.objects.create(
            title='Test Restaurant',
            place='Test Place',
            note='Test Note',
            image='path/to/test/image.jpg',
            type=self.type,
        )

        # Create User for review
        self.user = User.objects.create_user(
            username='test_user', password='test_password')

    def test_create_review(self):
        # Getting the URL for the createreview view with rest_id parameter
        # Получение URL-адреса для представления createreview с параметром rest_id
        url = reverse('restaurant:createreview', args=[self.restaurant.pk])

        # Preparing data to create a review
        data = {
            'note': 'Test Review Note',
            'user': self.user.pk,
            'stars': 4,
            'expenses': 50,
            'visit_date': timezone.now().date(),
        }

        # User authorization
        self.client.login(username='test_user', password='test_password')

        # Sending a POST request to create a review
        response = self.client.post(url, data)

        # Checking that the review was successfully created
        self.assertEqual(response.status_code, 302)

        # Checking that the review was actually added to the restaurant
        self.assertEqual(self.restaurant.reviews.count(), 1)

        # Check the contents of the review
        # Например, можно проверить содержимое отзыва:
        created_review = Review.objects.first()
        self.assertEqual(created_review.note, 'Test Review Note')
        self.assertEqual(created_review.stars, 4)
        self.assertEqual(created_review.expenses, 50)
