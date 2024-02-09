from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_quick_select_valid():
    response = client.post("/quickselect/", json={"array": [3, 2, 1, 5, 4], "k": 3})
    assert response.status_code == 200
    assert response.json() == {"kth_smallest_element": 3}

def test_quick_select_k_out_of_bounds():
    response = client.post("/quickselect/", json={"array": [1, 2, 3], "k": 5})
    assert response.status_code == 400
    assert response.json() == { "detail": "k is out of range" }

def test_quick_select_empty_array():
    response = client.post("/quickselect/", json={"array": [], "k": 1})
    assert response.status_code == 400
    assert response.json() == { "detail": "k is out of range" }
