import pytest
from rest_framework.test import APITestCase
from django.shortcuts import reverse
from conftest import EVERYTHING_EQUALS_NOT_NONE

pytestmark = [pytest.mark.django_db]


class TestGuestEndpoints(APITestCase):
    fixtures = ['catalog/tests/fixtures/categories_fixture.json', 'catalog/tests/fixtures/discount_fixture.json'
                'catalog/tests/fixtures/products_fixture.json', 'catalog/tests/fixtures/seller_fixture.json']

    def test_categories_list_endpoint(self):
        url = reverse('categories')
        response = self.client.get(url)
        assert response.status_code == 200
        assert isinstance(response.data, list)
        assert response.data == [
            {
                "id": 1,
                "name": EVERYTHING_EQUALS_NOT_NONE,
                "description": EVERYTHING_EQUALS_NOT_NONE
            },
            {
                "id": 2,
                "name": EVERYTHING_EQUALS_NOT_NONE,
                "description": EVERYTHING_EQUALS_NOT_NONE
            },
            {
                "id": 3,
                "name": EVERYTHING_EQUALS_NOT_NONE,
                "description": EVERYTHING_EQUALS_NOT_NONE
            },
            {
                "id": 4,
                "name": EVERYTHING_EQUALS_NOT_NONE,
                "description": EVERYTHING_EQUALS_NOT_NONE
            }

        ]

    def test_discount_list_endpoint(self):
        url = reverse('seller')
        response = self.client.get(url)
        assert response.status_code == 200
        assert isinstance(response.data, list)
        assert response.data == [
            {
                "id": 1,
                "name": EVERYTHING_EQUALS_NOT_NONE,
                "percent": EVERYTHING_EQUALS_NOT_NONE
            },
            {
                "id": 2,
                "name": EVERYTHING_EQUALS_NOT_NONE,
                "percent": EVERYTHING_EQUALS_NOT_NONE
            }
        ]
