from fastapi import APIRouter, HTTPException
from models import ArrayRequest
from services.statistics_service import find_kth_smallest_element

router = APIRouter()

@router.post("/quickselect/")
def quickselect_endpoint(request: ArrayRequest):
    try:
        result = find_kth_smallest_element(request.array, request.k)
        return {"kth_smallest_element": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))