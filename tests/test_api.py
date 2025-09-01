# tests/test_api.py
import requests

BASE_URL = "http://localhost:8000"

def test_list_customers():
    r = requests.get(f"{BASE_URL}/customers")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert len(data) > 0  # should have generated customers

def test_get_customer_by_id():
    r = requests.get(f"{BASE_URL}/customers/1")
    assert r.status_code == 200
    data = r.json()
    assert "id" in data
    assert "name" in data
    assert "email" in data

