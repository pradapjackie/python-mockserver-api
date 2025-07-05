

import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_user(client):
    response = client.get('/api/user/1')
    print("Response Status:", response.status_code)
    print("Response JSON:", response.get_json())
    assert response.status_code == 200
    assert response.json['user_id'] == 1

def test_create_user(client):
    response = client.post('/api/user', json={'name': 'New User'})
    print("Response Status:", response.status_code)
    print("Response JSON:", response.get_json())
    assert response.status_code == 201
    assert response.json['user']['name'] == 'New User'

def test_update_user(client):
    response = client.put('/api/user/1', json={'name': 'Updated'})
    print("Response Status:", response.status_code)
    print("Response JSON:", response.get_json())
    assert response.status_code == 200
    assert response.json['updates']['name'] == 'Updated'

def test_delete_user(client):
    response = client.delete('/api/user/1')
    print("Response Status:", response.status_code)
    print("Response JSON:", response.get_json())
    assert response.status_code == 200

def test_get_products(client):
    response = client.get('/api/products')
    print("Response Status:", response.status_code)
    print("Response JSON:", response.get_json())
    assert response.status_code == 200
    assert 'products' in response.json

def test_get_order(client):
    response = client.get('/api/order/100')
    print("Response Status:", response.status_code)
    print("Response JSON:", response.get_json())
    assert response.status_code == 200
    assert response.json['order_id'] == 100

def test_create_order(client):
    response = client.post('/api/order', json={'item': 'Book'})
    print("Response Status:", response.status_code)
    print("Response JSON:", response.get_json())
    assert response.status_code == 201
    assert response.json['order']['item'] == 'Book'

def test_login(client):
    response = client.post('/api/login', json={'username': 'admin'})
    print("Response Status:", response.status_code)
    print("Response JSON:", response.get_json())
    assert response.status_code == 200
    assert 'token' in response.json

def test_logout(client):
    response = client.post('/api/logout')
    print("Response Status:", response.status_code)
    print("Response JSON:", response.get_json())
    assert response.status_code == 200

def test_health_check(client):
    response = client.get('/api/health')
    print("Response Status:", response.status_code)
    print("Response JSON:", response.get_json())
    assert response.status_code == 200
    assert response.json['status'] == 'ok'

def test_get_notifications(client):
    response = client.get('/api/notifications')
    print("Response Status:", response.status_code)
    print("Response JSON:", response.get_json())
    assert response.status_code == 200
    assert isinstance(response.json['notifications'], list)

def test_get_settings(client):
    response = client.get('/api/settings')
    print("Response Status:", response.status_code)
    print("Response JSON:", response.get_json())
    assert response.status_code == 200
    assert 'theme' in response.json

def test_update_settings(client):
    response = client.put('/api/settings', json={'theme': 'light'})
    print("Response Status:", response.status_code)
    print("Response JSON:", response.get_json())
    assert response.status_code == 200
    assert response.json['settings']['theme'] == 'light'

def test_get_profile(client):
    response = client.get('/api/profile')
    print("Response Status:", response.status_code)
    print("Response JSON:", response.get_json())
    assert response.status_code == 200
    assert response.json['name'] == 'John Doe'

def test_update_profile(client):
    response = client.patch('/api/profile', json={'name': 'Jane'})
    print("Response Status:", response.status_code)
    print("Response JSON:", response.get_json())
    assert response.status_code == 200
    assert response.json['updates']['name'] == 'Jane'

def test_get_reports(client):
    response = client.get('/api/reports')
    print("Response Status:", response.status_code)
    print("Response JSON:", response.get_json())
    assert response.status_code == 200
    assert isinstance(response.json['reports'], list)

def test_upload_file(client):
    response = client.post('/api/upload')
    print("Response Status:", response.status_code)
    print("Response JSON:", response.get_json())
    assert response.status_code == 200
    assert 'file_id' in response.json