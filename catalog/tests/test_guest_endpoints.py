import pytest
from rest_framework.test import APITestCase
from django.shortcuts import reverse
from conftest import EVERYTHING_EQUALS_NOT_NONE

pytestmark = [pytest.mark.django_db]


class TestGuestEndpoints(APITestCase):
    fixtures = ['catalog/tests/fixtures/categories_fixture.json', 'catalog/tests/fixtures/discount_fixture.json',
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

    def test_discounts(self):
        url = reverse('discounts')
        response = self.client.get(url)
        assert response.status_code == 200
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

    def test_sellers(self):
        url = reverse('seller')
        response = self.client.get(url)
        assert response.status_code == 200
        assert response.data == [
            {
                "id": 1,
                "name": EVERYTHING_EQUALS_NOT_NONE,
                "description": EVERYTHING_EQUALS_NOT_NONE,
                "contact": EVERYTHING_EQUALS_NOT_NONE
            },
            {
                "id": 2,
                "name": EVERYTHING_EQUALS_NOT_NONE,
                "description": EVERYTHING_EQUALS_NOT_NONE,
                "contact": EVERYTHING_EQUALS_NOT_NONE
            },
            {
                "id": 3,
                "name": EVERYTHING_EQUALS_NOT_NONE,
                "description": EVERYTHING_EQUALS_NOT_NONE,
                "contact": EVERYTHING_EQUALS_NOT_NONE
            }
        ]

    def test_products(self):
        category = [1, 2, 3, 4]
        for category_id in category:
            url = reverse('category-products', kwargs={'category_id': category_id})
            response = self.client.get(url)
            assert response.status_code == 200
            assert isinstance(response.data, list)
            assert response.data == [
                {
                    "id": category_id,
                    "article": EVERYTHING_EQUALS_NOT_NONE,
                    "name": EVERYTHING_EQUALS_NOT_NONE,
                    "price": EVERYTHING_EQUALS_NOT_NONE
                }
            ]
