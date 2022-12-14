from fastapi.testclient import TestClient
from fastapi import status
import pytest, os

from main import app


client = TestClient(app)


def test_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {
        'message': 'I\'m a walnut'
    }

@pytest.mark.run(order=1)
def test_post_image():
    with open('test_image.jpg', 'rb') as f:
        test_image = f.read()
    response = client.post('/image', content=test_image)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.headers.get('Content-Location') == '/image.jpg'

@pytest.mark.run(order=2)
def test_get_image():
    with open('test_image.jpg', 'rb') as f:
        test_image = f.read()
    response = client.get('/image.jpg')
    assert response.status_code == status.HTTP_200_OK
    assert response.headers.get('Content-Type') == 'image/jpeg'
    assert response.content.__eq__(test_image)