from rest_framework.test import APIClient
import pytest

@pytest.fixture
def api_client(initial_data):
    return APIClient()