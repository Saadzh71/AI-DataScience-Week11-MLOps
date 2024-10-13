from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_prediction():
    response = client.post("/prediction", json={
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    })
    assert response.status_code == 200
    assert "prediction" in response.json()