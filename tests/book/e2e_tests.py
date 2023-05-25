from rest_framework.test import APIClient
import pytest

pytestmark = [
    pytest.mark.django_db(databases=["default"]),
    pytest.mark.e2e,
    pytest.mark.book,
]


class TestBookEndpoints:
    endpoint = "/api/retrieve-book"

    def test_retrieve_book(self, mocker, api_client: APIClient):
        response = api_client.get(path=f"{self.endpoint}")
        assert response.status_code == 200