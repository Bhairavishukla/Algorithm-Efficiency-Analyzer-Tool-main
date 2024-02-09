
## Getting Started

### Project Structure

The project is organized into the following directories and files:

- **routers/**: Contains route definitions for the API. Includes `median.py`, `quickselect.py`, and `sort.py` for handling requests related to median calculation, quickselect operations, and sorting arrays respectively.
- **services/**: Contains business logic for sorting and statistical operations. Includes `sort_service.py` and `statistics_service.py`.
- **sorting_algorithms/**: Implements various sorting algorithms.
- **tests/**: Contains test cases for the API functionalities. Includes `test_quick_select.py` and `test_sort_api_multiple_algorithms.py`.
- **config.py**: Configuration settings, including CORS settings.
- **main.py**: The FastAPI application setup and entry point.
- **models.py**: Pydantic models for request and response schemas.
- **README.md**: This file, providing an overview and documentation.
- **requirements.txt**: Lists the project's dependencies.
- **supported_algorithms.py**: Maps algorithm names to their corresponding implementation functions for easy lookup.

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository:**  ```git clone https://github.com/abhishekbuilds/Algorithm-Efficiency-Analyzer-Tool/tree/main/backend```

2. **Navigate to the project directory:**  ```cd algorithm-efficiency-analyzer-tool/backend```

3. **Install required dependencies:**  ```pip install -r requirements.txt```

### Running the Application

1. **Start the FastAPI server:**  
    
    ```uvicorn main:app --reload```
    
    The API will be available at `http://127.0.0.1:8000`.

### Using the API

- **Sort an Array**: POST `/sort/`
  Send a POST request to `/sort/` with a JSON body specifying the `array` and `algorithms`. Example:

  ```json
  {
    "array": [34, 7, 23, 32, 5, 62],
    "algorithms": ["insertion_sort", "selection_sort", "merge_sort"]
  }
  ```

  Use tools like `curl`, Postman, or any HTTP client to make the request.
- **Find the Median**: POST `/median/`
  Send a POST request to `/median/` with a JSON body specifying `array` list. Example:

  ```json
  {
    "array": [34, 7, 23, 32, 5, 62]
  }
  ```
- **QuickSelect Operation**: POST `/quickselect/`
  Send a POST request to `/quickselect/` with a JSON body specifying `array` list and position `k`. Example:

  ```json
  {
    "array": [34, 7, 23, 32, 5, 62],
    "k": 3
  }
  ```

## Development

### Adding New Algorithms

1. Implement the new sorting algorithm in `sorting_algorithms/`.
2. Update `supported_algorithms.py` to include the new algorithm.

### Running Tests

Run tests using pytest:

```
pytest tests/* 
```