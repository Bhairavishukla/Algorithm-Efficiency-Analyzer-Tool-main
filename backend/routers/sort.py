from fastapi import APIRouter, HTTPException
from models import ArrayRequest
from services.sort_service import execute_sorting_algorithm
from services.statistics_service import find_kth_smallest_element

router = APIRouter()

@router.post("/sort/")
def sort_array(request: ArrayRequest):
    results = []
    for algorithm_name in request.algorithms:
        if algorithm_name.lower() == "quick_select":
            if not hasattr(request, 'k') or request.k is None:
                raise HTTPException(status_code=400, detail="k is required for QuickSelect")
            try:
                result = find_kth_smallest_element(request.array, request.k)
                results.append(result)
            except ValueError as e:
                raise HTTPException(status_code=400, detail=str(e))
        else:
            result = execute_sorting_algorithm(algorithm_name, request.array.copy())
            if result is None:
                raise HTTPException(status_code=400, detail=f"Algorithm '{algorithm_name}' not supported")
            results.append(result)
    return results