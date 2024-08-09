from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_generate_image():
    response = client.get("/generate-image/?prompt=A sunny day")
    assert response.status_code == 200
    assert "image_path" in response.json()
