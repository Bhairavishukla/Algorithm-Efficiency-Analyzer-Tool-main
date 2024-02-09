from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_sort_with_multiple_algorithms():
    response = client.post(
        "/sort/",
        json={
            "array": [5, 3, 8, 4, 2],
            "algorithms": ["insertion_sort", "selection_sort", "merge_sort"]
        },
    )
    assert response.status_code == 200
    data = response.json()
    
    assert len(data) == 3
    
    expected_sorted_array = [2, 3, 4, 5, 8]
    assert data[0]["sortedArray"] == expected_sorted_array
    
    expected_names = ["Insertion Sort", "Selection Sort", "Merge Sort"]
    for i, algorithm_response in enumerate(data):
        assert algorithm_response["name"] == expected_names[i]
        assert isinstance(algorithm_response["timeTaken"], float)